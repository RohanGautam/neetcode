class Solution:
    def findMin(self, nums: List[int]) -> int:
        # key facts:
        # - array was originally sorted. 
        # - has been rotated between 1 and len(arr) times
        # - all elements are unique
        l,u = 0, len(nums)-1
        while l<=u:
            m = l+(u-l)//2
            print(l,u,m)
            # if nums[m]<nums[l]:
            #     # problematic pivot between m and l
            #     u=m
            # elif nums[m]>nums[l]:
            #     l=m+1
            # else:
            #     break
            # attempt 2: need to compare with upper instead
            if nums[m]<nums[u]:
                # fine, problem in other half
                u=m 
            elif nums[m]>nums[u]:
                l=m+1
            else:
                break
        # pivot point is now l=m
        # print(l)
        # if u>1 and u==len(nums)-1 and u-1==l:
        #     return nums[0]

        return nums[(u)%len(nums)]