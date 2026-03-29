class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        # here, the difference is that each hting must be chosen at most once
        result = []
        # SORT UT!!
        nums = sorted(nums)

        def bt(index, path):
            if sum(path)==target:
                result.append(path[:])
                return
            elif sum(path)>target:
                return
            else:
                prev = None
                for i in range(index,len(nums)):
                    # dont start two branches in the same loop if they happen more than once.
                    # those will find the same solution otherwise
                    if nums[i]!=prev:
                        # remember, path mutated
                        path.append(nums[i])
                        # i+1 as you dont consider this anymore, it's considered in the path
                        bt(i+1,path)
                        # remove
                        path.pop()
                        prev=nums[i]
        bt(0,[])
        return result