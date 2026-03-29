class Solution:
    def minEatingSpeed(self, piles: List[int], hours: int) -> int:
        l,h=1,max(piles)
        k_opt=h
        while l<=h:
            k_guess = l+((h-l)//2)
            # calculate t
            t = 0
            for p in piles:
                t += p//k_guess
                if p%k_guess>0:
                    t+=1
            if t>hours:
                # lower k is a higher time, so increase k guess
                # want to decrease time, so increase k
                l=k_guess+1
            elif t<=hours:
                if k_guess<k_opt:
                    k_opt=k_guess
                # see if a higher time exists - will lead to smaller k
                h=k_guess-1
        return k_opt