class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        cur=0
        for n in nums:
            # if cur<0:
            #     cur=0
            # cur+=n
            # captures the previous logic well
            cur = max(n, cur+n)
            res=max(res,cur)
        return res