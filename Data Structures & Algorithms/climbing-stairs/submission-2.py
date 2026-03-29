class Solution:
    def climbStairs(self, n: int,d={1:1,2:2}) -> int:
        if n in d:
            return d[n]
        # modifies (shallow copy) across the recursive call stack
        d[n] = self.climbStairs(n-1)+self.climbStairs(n-2)
        return d[n]
        