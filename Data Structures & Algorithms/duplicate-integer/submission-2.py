class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # have to be O(n) time and O(n) space
        s = set()
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                return True
        return False