class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # return all solutions, not optimal solution
        # hence backtracking, not dp
        # also, same number can be chosen unlimited number of times
        result = []

        def bt(path):
            if sum(path)==target:
                result.append(sorted(path[:]))
                return # try other branches
            
            # go through choices we have:
            for n in nums:
                # check if valid to add 
                if sum(path)+n<=target and sorted(path+[n]) not in result:
                    # using like it's dfs
                    bt(path+[n])
        bt([])
        return result
            
