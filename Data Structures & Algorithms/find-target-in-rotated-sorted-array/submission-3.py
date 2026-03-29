class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # as with the previous rotated question,
        # - unique elements
        # - originally sorted
        # - rotated between 1 and len(list) times

        # first idea: find the pivot, then use a binary search that takes this into account
        l,u= 0,len(nums)-1
        while l<u:
            m=l+((u-l)//2)
            if nums[m]<nums[u]:
                u=m
            else:
                l=m+1
        print(u) #u is the pivot index+1
        pivot_idx=u
        idx_map = lambda x: (x+pivot_idx)%len(nums)

        l,u= 0,len(nums)-1
        loc=None
        while l<=u:
            m=l+((u-l)//2)
            # print(l,u,m, idx_map(l), idx_map(u), idx_map(m))
            # print('#---')
            if target>nums[idx_map(m)]:
                l=m+1
            elif target<nums[idx_map(m)]:
                u=m-1
            else:
                loc=m
                # print("found")
                # print(loc)
                break
        if loc is None:
            return -1
        return idx_map(loc)
