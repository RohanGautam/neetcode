class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for e in nums:
            if e not in dup:
                dup.add(e)
            else:
                return True
        return False

         