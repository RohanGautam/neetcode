class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # there are duplicates, but cant have duplicate subsets
        # we handled it with a sort for perms i think
        nums.sort()
        results = []

        def bt(index, path):
            if index==len(nums) and path not in results:
                results.append(path[:])
                return
            elif index>=len(nums):
                return
            
            path.append(nums[index])
            bt(index+1, path)
            path.pop()
            bt(index+1, path)
        bt(0,[])
        return results
        