class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        l=0
        total = 0
        # u is the upper pointer
        for u in range(len(s)):
            while s[u] in seen:
                seen.remove(s[l])
                l+=1
            seen.add(s[u])
            total = max(total, u-l+1)
        return total
