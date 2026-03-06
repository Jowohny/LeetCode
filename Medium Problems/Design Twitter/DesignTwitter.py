class Twitter:
    def __init__(self):

        #global timer to simulate time for each tweet
        self.timer = 0

        #use a dictionary to match each tweet to their user
        self.tweets = collections.defaultdict(list)

        #use another dictionary to find each person's followers
        self.following = collections.defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        #when assigning a tweet to a time, decrement it to give it a more negative value
        #by making the time the key of the heap, using negative values make a max heap, popping the most negative time
        self.timer -= 1

        #add the current tweet to the dictionary to the associated user in the dictionary
        self.tweets[userId].append((self.timer, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        #since the users see their own feed amongst others, add the user to their own follower set
        self.following[userId].add(userId)

        #go through every follower in the current user's follower list
        for followeeId in self.following[userId]:
            if followeeId in self.tweets:

                #get the time of the latest tweet from this user
                #using the time, unpack the latest tweet from this user
                lastId = len(self.tweets[followeeId]) - 1
                time, tId = self.tweets[followeeId][lastId]

                #push (timestamp, tweetId, followeeId, next_index_to_check)
                heapq.heappush(heap, (time, tId, followeeId, lastId - 1))

        #only get the 10 most recent tweets
        while heap and len(res) < 10:
            time, tId, fId, nextId = heapq.heappop(heap)
            res.append(tId)

            #if this user has more tweets, push the next most recent one into the heap
            if nextId >= 0:
                nextTime, nextIdx = self.tweets[fId][nextId]
                heapq.heappush(heap, (nextTime, nextIdx, fId, nextId - 1))

        #return the list of ids found, representing the current followees twitter feed
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        #add the followee to the follower's set
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #remove the followee if they exist in the set and it's not the user themselves
        if followeeId in self.following[followerId] and followerId != followeeId:
            self.following[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)