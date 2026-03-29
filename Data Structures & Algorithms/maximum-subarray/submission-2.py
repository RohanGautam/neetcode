class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # need to also track the maximum because things can get overwritten later on
        maxval=nums[0]
        s = 0
        for n in nums:
            if s<0:
                s=0
            s+=n
            maxval=max(maxval,s)
        return maxval