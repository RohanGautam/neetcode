class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []

        def bt(index, path):
            if index==len(nums):
                results.append(path[:])
                return
            
            # consider current element
            path.append(nums[index])
            bt(index+1, path)
            path.pop()

            # next element you consider should be not a duplicate of current
            i=index+1
            while i<len(nums) and nums[i]==nums[index]:
                i+=1
            bt(i, path)
        bt(0,[])
        return results
        