class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.post_map = defaultdict(list)
        self.time_to_post = {}
        self.time = 0
        self.limit = 10
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_map[userId].append(self.time)
        self.time_to_post[self.time] = tweetId
        self.time -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        self.follow_map[userId].add(userId)
        
        min_heap = []
        for followee_id in self.follow_map[userId]:
            if self.post_map[followee_id]:
                min_heap.append((self.post_map[followee_id][-1], followee_id, -1))
        heapq.heapify(min_heap)
        
        feed = []
        while min_heap and len(feed) != 10:
            post_time, followee_id, curr_idx = heapq.heappop(min_heap)
            feed.append(self.time_to_post[post_time])
            next_idx = curr_idx - 1
            if next_idx >= -len(self.post_map[followee_id]):
                next_post_time = self.post_map[followee_id][next_idx]
                heapq.heappush(min_heap, (next_post_time, followee_id, next_idx))
        
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)