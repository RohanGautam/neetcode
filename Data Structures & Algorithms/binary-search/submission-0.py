class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h = 0, len(nums)-1
        # nums is sorted so we use binary search
        while l<=h:
            print(l,h)
            m = l + ((h-l)//2)
            if target>nums[m]:
                l=m+1
            elif target<nums[m]:
                h=m-1
            else:
                return m
        return -1
        