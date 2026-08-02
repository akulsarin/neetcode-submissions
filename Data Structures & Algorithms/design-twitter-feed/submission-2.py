class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.timestamp = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.timestamp, tweetId))
        self.timestamp -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        returnIds = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            followeeTweets = self.tweetMap[followee]
            numPosts = len(followeeTweets)
            if numPosts > 0:
                timestamp, tweetId = followeeTweets[numPosts - 1]
                heapq.heappush(minHeap, (timestamp, tweetId, followee, numPosts - 2))

        while minHeap and len(returnIds) < 10:
            ts, tweetId, followeeId, nextIdx = heapq.heappop(minHeap)
            returnIds.append(tweetId)
            if nextIdx >= 0:
                nextTs, nextTweetId = self.tweetMap[followeeId][nextIdx]
                heapq.heappush(minHeap, (nextTs, nextTweetId, followeeId, nextIdx - 1))
        
        return returnIds

        
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
