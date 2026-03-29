class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path=[]
        def bt(pos):
            if sum(path)==target:
                res.append(path[:])
            
            if not (pos<len(nums) and sum(path)<target):
                return
            path.append(nums[pos])
            bt(pos)
            path.pop()
            bt(pos+1)
        bt(0)
        return res