class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # but with acktracking - we want to learn it after all
        results = []
        def backtrack(index, path):
            if index==len(nums):
                # element with index has already been considered
                results.append(path[:]) # deep copy
                return
            
            path.append(nums[index])
            backtrack(index+1, path)
            path.pop()
            backtrack(index+1,path)

        backtrack(0,[])
        return results