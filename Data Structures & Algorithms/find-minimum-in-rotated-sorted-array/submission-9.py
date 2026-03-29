class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search once you find rotation offset.
        l,u = 0, len(nums)-1
        offset=0
        while l<=u:
            m=l+(u-l)//2
            print(l,u,m)
            # we are searching for anomalies with respect to u
            if nums[m]>=nums[u]:
                # problematic, because m should be less in a properly sorted array
                offset=m
                # but could also be something after m
                l=m+1
            elif nums[m]<nums[u]:
                # look before m
                # Note: not m-1!!!!
                u=m
        print(u)            
        return nums[u]
                  