package cc.sovellus.vrcaa.data.friends

import cc.sovellus.vrcaa.base.BaseClient
import kotlinx.coroutines.CancellationException
import kotlinx.coroutines.runBlocking
import okhttp3.Protocol
import okhttp3.Request
import okhttp3.Response
import org.junit.Assert.*
import org.junit.Test

class FriendsRepositoryTest {
    private fun succeeded(body: String): BaseClient.Result.Succeeded {
        val response = Response.Builder().request(Request.Builder().url("https://example.invalid").build())
            .protocol(Protocol.HTTP_1_1).code(200).message("OK").build()
        return BaseClient.Result.Succeeded(response, body)
    }

    @Test fun validEmptyPageIsSuccess() = runBlocking {
        val repository = LegacyFriendsRepository { succeeded("[]") }
        assertEquals(FriendsResult.Success(FriendsPage(emptyList(), null)), repository.fetchPage(FriendsQuery(false)))
    }

    @Test fun failuresNeverBecomeEmptySuccess() = runBlocking {
        val cases = mapOf(
            BaseClient.Result.NoInternet to FriendsError.Offline,
            BaseClient.Result.Unauthorized to FriendsError.Unauthorized,
            BaseClient.Result.Forbidden to FriendsError.Forbidden,
            BaseClient.Result.RateLimited to FriendsError.RateLimited,
            BaseClient.Result.InternalError to FriendsError.Server,
            BaseClient.Result.NotModified to FriendsError.UnexpectedResponse,
            BaseClient.Result.NotFound to FriendsError.UnexpectedResponse,
        )
        for ((result, error) in cases) {
            assertEquals(FriendsResult.Failure(error), LegacyFriendsRepository { result }.fetchPage(FriendsQuery(false)))
        }
    }

    @Test fun oneRequestPreservesQueryAndProjectsOnlyRequiredFields() = runBlocking {
        var calls = 0
        val query = FriendsQuery(true, 1, 100)
        val repository = LegacyFriendsRepository {
            calls++
            assertEquals(query, it)
            succeeded("""[{"id":"fixture-1","displayName":"Orbit","status":"unknown-future-status","location":"private"}]""")
        }
        assertEquals(FriendsResult.Success(FriendsPage(listOf(FriendSummary("fixture-1", "Orbit", "unknown-future-status")), 101)), repository.fetchPage(query))
        assertEquals(1, calls)
    }

    @Test fun malformedOrIncompletePayloadIsFailure() = runBlocking {
        for (body in listOf("null", "{}", "not json", "[null]", "[{}]",
            """[{"id":12,"displayName":"Orbit"}]""",
            """[{"id":" ","displayName":"Orbit"}]""",
            """[{"id":"fixture-1","displayName":"Orbit"},{"id":"fixture-1","displayName":"Other"}]""")) {
            assertEquals(body, FriendsResult.Failure(FriendsError.InvalidPayload),
                LegacyFriendsRepository { succeeded(body) }.fetchPage(FriendsQuery(false)))
        }
    }

    @Test fun nonJsonSyntaxCannotPublishAFriendPage() = runBlocking {
        // A tolerated JavaScript-like payload must not become a valid API snapshot.
        for (body in listOf(
            """[{'id':'fixture-1','displayName':'Orbit'}]""",
            """[{id:"fixture-1",displayName:"Orbit"}]""",
            """/* cached response */ [{"id":"fixture-1","displayName":"Orbit"}]""",
            """[{"id":"fixture-1","displayName":"Orbit"}] trailing""",
        )) {
            assertEquals(body, FriendsResult.Failure(FriendsError.InvalidPayload),
                LegacyFriendsRepository { succeeded(body) }.fetchPage(FriendsQuery(false)))
        }
    }

    @Test fun mutatingAReturnedFakePageCannotChangeLaterReads() = runBlocking {
        val rows = listOf(
            FriendSummary("fixture-1", "Orbit One", "active"),
            FriendSummary("fixture-2", "Orbit Two", "active"),
        )
        val repository = FakeFriendsRepository(rows)
        val first = repository.fetchPage(FriendsQuery(false)) as FriendsResult.Success
        // Kotlin List is read-only at the call site, but Java/interop consumers may mutate it.
        try {
            @Suppress("UNCHECKED_CAST")
            (first.page.friends as MutableList<FriendSummary>).clear()
        } catch (_: UnsupportedOperationException) {
            // An unmodifiable result also satisfies isolation.
        }
        val second = repository.fetchPage(FriendsQuery(false)) as FriendsResult.Success
        assertEquals(rows, second.page.friends)
    }

    @Test fun oversizedPageIsRejected() = runBlocking {
        val body = """[{"id":"fixture-1","displayName":"One"},{"id":"fixture-2","displayName":"Two"}]"""
        assertEquals(FriendsResult.Failure(FriendsError.InvalidPayload),
            LegacyFriendsRepository { succeeded(body) }.fetchPage(FriendsQuery(false, 1)))
    }

    @Test fun missingStatusRemainsUnknownRatherThanOffline() = runBlocking {
        val result = LegacyFriendsRepository { succeeded("""[{"id":"fixture-1","displayName":"Orbit"}]""") }
            .fetchPage(FriendsQuery(false)) as FriendsResult.Success
        assertEquals("", result.page.friends.single().status)
        assertNull(result.page.nextOffset)
    }

    @Test fun fakeAndLegacyHaveSamePaginationContract() = runBlocking {
        val rows = listOf(FriendSummary("fixture-1", "Orbit", "active"))
        val fake: FriendsRepository = FakeFriendsRepository(rows)
        val legacy: FriendsRepository = LegacyFriendsRepository {
            succeeded(if (it.offset == 0) """[{"id":"fixture-1","displayName":"Orbit","status":"active"}]""" else "[]")
        }
        for (offset in listOf(0, 1)) {
            val query = FriendsQuery(false, 1, offset)
            assertEquals(legacy.fetchPage(query), fake.fetchPage(query))
        }
        assertEquals(FriendsResult.Success(FriendsPage(emptyList(), null)), fake.fetchPage(FriendsQuery(true)))
    }

    @Test fun fakeCopiesInputAndSupportsTypedFailure() = runBlocking {
        val input = mutableListOf(FriendSummary("fixture-1", "Orbit", "active"))
        val fake = FakeFriendsRepository(input)
        input.clear()
        assertEquals(1, (fake.fetchPage(FriendsQuery(false)) as FriendsResult.Success).page.friends.size)
        assertEquals(FriendsResult.Failure(FriendsError.RateLimited),
            FakeFriendsRepository(error = FriendsError.RateLimited).fetchPage(FriendsQuery(false)))
    }

    @Test fun cancellationPropagatesWithoutRetry() = runBlocking {
        var calls = 0
        try {
            LegacyFriendsRepository { calls++; throw CancellationException("test cancellation") }.fetchPage(FriendsQuery(false))
            fail("Cancellation must propagate")
        } catch (_: CancellationException) {
            assertEquals(1, calls)
        }
    }

    @Test fun invalidQueriesFailBeforeAnyRequest() {
        for ((limit, offset) in listOf(0 to 0, 101 to 0, 1 to -1, 100 to Int.MAX_VALUE)) {
            assertThrows(IllegalArgumentException::class.java) { FriendsQuery(false, limit, offset) }
        }
    }
}
