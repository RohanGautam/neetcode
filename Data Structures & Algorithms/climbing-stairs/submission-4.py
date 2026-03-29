class Solution:
    def climbStairs(self, n: int,d={1:1,2:2}) -> int:
        if n in d:
            return d[n]

        # reach the current step with just one or two steps taken from before.
        # the number of steps is not what we want, but the number of ways, so
        # thats why we're not adding any integers here
        # also, d is modified in place so everything else in the call stack 
        # can see when we make a change anywhere
        d[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return d[n]