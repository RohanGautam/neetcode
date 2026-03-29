class Solution:
    def climbStairs(self, n: int,d={1:1,2:2}) -> int:
        if n in d:
            return d[n]


        c1= self.climbStairs(n-1, d=d)
        d[n-1]=c1
        c2 = self.climbStairs(n-2, d=d)
        d[n-2]=c2
        return c1+c2
        