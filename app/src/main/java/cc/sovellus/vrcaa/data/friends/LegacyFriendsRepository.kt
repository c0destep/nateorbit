package cc.sovellus.vrcaa.data.friends

import cc.sovellus.vrcaa.base.BaseClient
import com.google.gson.GsonBuilder
import com.google.gson.JsonElement
import com.google.gson.JsonParseException
import com.google.gson.Strictness

/** Adapts one legacy request; never calls the old recursive, error-swallowing fetchFriends. */
class LegacyFriendsRepository(
    private val request: suspend (FriendsQuery) -> BaseClient.Result,
) : FriendsRepository {
    private val gson = GsonBuilder().setStrictness(Strictness.STRICT).create()

    override suspend fun fetchPage(query: FriendsQuery): FriendsResult = when (val result = request(query)) {
        is BaseClient.Result.Succeeded -> decode(result.body, query)
        BaseClient.Result.NoInternet -> failure(FriendsError.Offline)
        BaseClient.Result.Unauthorized -> failure(FriendsError.Unauthorized)
        BaseClient.Result.Forbidden -> failure(FriendsError.Forbidden)
        BaseClient.Result.RateLimited -> failure(FriendsError.RateLimited)
        BaseClient.Result.InternalError -> failure(FriendsError.Server)
        else -> failure(FriendsError.UnexpectedResponse)
    }

    private fun decode(body: String, query: FriendsQuery): FriendsResult {
        try {
            val json = gson.fromJson(body, JsonElement::class.java)
            if (json == null || !json.isJsonArray || json.asJsonArray.size() > query.limit) return failure(FriendsError.InvalidPayload)
            val friends = json.asJsonArray.map { element ->
                require(element.isJsonObject)
                val obj = element.asJsonObject
                fun string(name: String, required: Boolean): String {
                    val value = obj.get(name)
                    if (value == null || value.isJsonNull) {
                        require(!required)
                        return ""
                    }
                    require(value.isJsonPrimitive && value.asJsonPrimitive.isString)
                    return value.asString.also { require(!required || it.isNotBlank()) }
                }
                FriendSummary(string("id", true), string("displayName", true), string("status", false))
            }
            require(friends.map { it.id }.distinct().size == friends.size)
            return FriendsResult.Success(FriendsPage(friends, if (friends.size == query.limit) query.offset + query.limit else null))
        } catch (_: JsonParseException) {
            return failure(FriendsError.InvalidPayload)
        } catch (_: IllegalArgumentException) {
            return failure(FriendsError.InvalidPayload)
        }
    }

    private fun failure(error: FriendsError) = FriendsResult.Failure(error)
}
