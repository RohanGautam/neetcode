import heapq
from collections import defaultdict
class Twitter:

    def __init__(self):
        # store user: who user follows
        self.d=defaultdict(set)
        self.tweets=defaultdict(list)
        self.count=0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        # still need the count for nerging and getting latest stuff later
        self.tweets[userId].append((self.count,tweetId))
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        # defaultdict handles non existence cases
        # relevant_tweets = [self.tweets[f][:] for f in self.d[userId]] + [self.tweets[userId][:]]
        # print(userId, relevant_tweets)
        # heap = []
        # i,n=0,len(relevant_tweets)
        # while len(heap)<10 and any(relevant_tweets):
        #     if relevant_tweets[i%n]:
        #         heapq.heappush(heap, relevant_tweets[i%n].pop())
        #     i+=1
        # res = []
        # while len(res)<10 and heap:
        #     res.append(heapq.heappop(heap)[-1])
        # print(res)
        # return res
        # self.d[userId].add(userId) # including the user itself.
        heap,frontier = [],[]
        # track info from last eles of the followers (including itself)
        # set union : slick!
        for fid in self.d[userId]|{userId}:
            # get their most recent tweet
            if fid in self.tweets:
                index = len(self.tweets[fid])-1 # the last ele
                if index>=0:
                    count, tid = self.tweets[fid][index]
                    # index is the next index in the same list to check
                    # frontier.append([fid, count, index])
                    # this will be O(FlogF) if F is the frontier size
                    # heapq.heappush(heap, (count, fid,tid, index-1))
                    frontier.append((count, fid,tid, index-1))
        heapq.heapify(frontier) # in place, O(F)
        heap=frontier
        res=[]
        while len(res)<10 and heap:
            _, fid,tid, index = heapq.heappop(heap)
            res.append(tid)
            if index>=0:
                # add element lower to the heap
                count, tid = self.tweets[fid][index]
                heapq.heappush(heap, (count, fid, tid, index-1))
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId!=followeeId:
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

Reflections:
- initial attempt was NlogN where N was the total number of tweets in twitter.
- If you look up tweets just for the followers then you consider a much smaller subset of tweets.
- However, this could still be NlogN if everyone follows everyone
- If you used a key->list mapping for tweets posted per user, you'd fetch those lists
    - But you dont have to iterate all! Just take the frontier of the lists (last values of all), add to a minheap until the minheap length is 10
    - if n is the number of followee ids(in the qn) this will be O(nlogn)(each end value pushed to heap) to build heap and O(10logn) to retrieve
    - Here's a cool fact about heap! You can build a heap by pushing n eles one by 1 (O(nlogn)) or use heapify (O(N) - more eff cus uses floyds algorithm)
    - but even if you add 1 by 1, the complexity will be O(nlogn), which is reccomended by the qn
    - todo: Compare with naive merge k sorted list approach in detail, mentioned in the video
- Issue: Cant just keep taking from just the frontier: if top3 and 3 peple, chances are all 3 most recent tweets can be from the same person.
- Add all frontier elements at level 1 first. Then, add the min to a heap, replace the min in the heap with the next one! continue this process.
'''