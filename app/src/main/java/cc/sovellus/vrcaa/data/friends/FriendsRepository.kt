package cc.sovellus.vrcaa.data.friends

/** Read-only boundary. One page is not a complete snapshot or proof of deletion. */
interface FriendsRepository {
    suspend fun fetchPage(query: FriendsQuery): FriendsResult
}

data class FriendsQuery(val offline: Boolean, val limit: Int = 100, val offset: Int = 0) {
    init {
        require(limit in 1..100)
        require(offset in 0..(Int.MAX_VALUE - limit))
    }
}

/** Minimal immutable projection; no credentials, private locations or mutable legacy DTOs. */
data class FriendSummary(val id: String, val displayName: String, val status: String)

data class FriendsPage(val friends: List<FriendSummary>, val nextOffset: Int?)

sealed interface FriendsResult {
    data class Success(val page: FriendsPage) : FriendsResult
    data class Failure(val error: FriendsError) : FriendsResult
}

enum class FriendsError {
    Offline, Unauthorized, Forbidden, RateLimited, Server, InvalidPayload, UnexpectedResponse
}

/** Synthetic data only. Failures never masquerade as a successful empty page. */
class FakeFriendsRepository(
    online: List<FriendSummary> = listOf(FriendSummary("fixture-orbit-1", "Orbit One", "active")),
    offline: List<FriendSummary> = emptyList(),
    private val error: FriendsError? = null,
) : FriendsRepository {
    private val online = online.toList()
    private val offline = offline.toList()

    override suspend fun fetchPage(query: FriendsQuery): FriendsResult {
        error?.let { return FriendsResult.Failure(it) }
        val source = if (query.offline) offline else online
        val page = source.drop(query.offset).take(query.limit)
        // Like the endpoint, a full page requires another request to prove exhaustion.
        return FriendsResult.Success(FriendsPage(page, if (page.size == query.limit) query.offset + query.limit else null))
    }
}
