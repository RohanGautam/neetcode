class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # if len(nums)==0:
        #     return [[]]
        # prev_sets = self.subsets(nums[:-1])
        # additional_sets=[prev_sets[i]+[nums[-1]] for i in range(len(prev_sets))]
        # # print(nums, prev_sets, additional_sets)
        # return prev_sets+additional_sets
        res = [[]]
        for n in nums:
            res.extend([x+[n] for x in res])
        return res
