class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        # prev approach was dfs. also used sorting for the "ordering" but backtracking just uses the index, not allowing you to look back
        def bt(index,path):
            if sum(path)==target:
                result.append(path[:])
                return 
            elif sum(path)>target:
                return
            else:
                for i in range(index,len(nums)):
                    path.append(nums[i])
                    bt(i,path) # not i+1 since you can reuse
                    path.pop()
        bt(0,[])
        return result
