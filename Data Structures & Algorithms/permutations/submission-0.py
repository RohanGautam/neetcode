class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        def bt(path):
            # cant be index based since last index can be in the middle
            if len(path)==len(nums):
                result.append(path[:])
                return
                
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    bt(path)
                    # so that next iteration of the loop starts with a fresh state
                    path.pop()
        bt([])
        return result