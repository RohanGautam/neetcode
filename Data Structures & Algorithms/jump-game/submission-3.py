class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # cache, will have true if valid
        d={}
        def dfs(index):
            if index>=len(nums):
                return False
            elif index==len(nums)-1:
                # we've reached the end
                return True

            # cache mechanism
            if index in d:
                return d[index]

            n = nums[index]
            for x in range(1,n+1):
                res = dfs(index+x)
                if res:
                    return True
                d[x]=res
            return False
        return dfs(0)
            