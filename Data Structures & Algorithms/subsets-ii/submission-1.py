class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        def bt(index, path):
            # if index==len(nums):
            # valid subset each time you enter
            results.append(path[:])
                # return
            
            for i in range(index,len(nums)):
                if i!=index and nums[i]==nums[i-1]:
                    continue                
                path.append(nums[i])
                bt(i+1, path)
                path.pop()
                # for loop manages exploring other options, so dont need this explicitly
                # bt(i+1, path)
        bt(0,[])
        return results
        