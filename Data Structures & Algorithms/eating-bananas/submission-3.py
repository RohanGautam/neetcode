import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # nice because it's blind right now, i dont know the topic theme.
        # min banana eating rate to eat all bananas, one pile at a time.
        # the monkey wants to eat as slow as possible.
        # search for min k ! but be clever and use binary search. 
        # you can use binary search because the sumof the number of hours it takes
        # decreases with increasing k - but it's still implicitly "sorted" in that sese.

        # with max(piles), the number of hourse will be the number of piles, which is as fast as you'd need to eat
        # O(n)
        l,u = 1, max(piles)
        res=u
        while l<=u:
            k = l+((u-l)//2)
            # O(n)
            time_taken = sum(max(1, math.ceil(i/k)) for i in piles)
            if time_taken>h:
                # eat faster
                l=k+1
            elif time_taken<=h:
                # slow down and check, but keep track in case this is the best one
                # this is still a valid k
                res=min(res, k)
                # see if eating even slower works
                u=k-1
                # equality doesnt need to be checked here as the opt might be a less
        return res