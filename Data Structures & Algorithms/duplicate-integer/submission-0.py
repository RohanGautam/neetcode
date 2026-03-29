class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = []
        for e in nums:
            if e not in dup:
                dup.append(e)
            else:
                return True
        return False

         