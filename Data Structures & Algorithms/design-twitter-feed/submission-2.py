class Twitter:

    def __init__(self):
        # store user: who user follows
        self.d={}
        self.tweets=[]
        self.count=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId,tweetId, self.count))
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = [(ti,c) for ui,ti,c in self.tweets if ui==userId or (userId in self.d and ui in self.d[userId])]
        res =  sorted(res,key=lambda x: x[-1])
        return [x[0] for x in res][:10]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.d:
            self.d[followerId]=set()
        self.d[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.d and followeeId in self.d[followerId]:
            self.d[followerId].remove(followeeId)
        

'''
observations
- each tweetid is unique
- look up 10 most recent tweets that the user/their followers posted
- follow/unfollow mechanism

st1: simple way
    - follow/unfollow : modify a {user_id:[follower_id]} hashmap
    - postTweet: append to [(user_id,tweet_id, count-1)] (count init=0)
    - getnewsfeed: sort by count (smaller = more recent), filter by followers, return result

observations:
    - sorting is O(nlogn) each time - maybe have a minheap? 
    - actually, a minheap of size 10 for each user
    - still O(n) memory -> getting news feed becomes O(10)=O(1)
    - posttweet : O(1)->O(n): dont want this in the real world
    - goal: O(nlogn) for getnewsfeed, O(1) for the rest
    - st_1 is already this - except for unfollow
    - store follow/unfollow in {user_id: set([follower_id])} -> O(1) adding AND removing
'''