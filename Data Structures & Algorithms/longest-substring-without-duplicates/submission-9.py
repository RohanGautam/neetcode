class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintain char:frequency
        # actually, only need a set
        d=set()
        l=0
        res = 0
        for u in range(len(s)):
            # while sum(d.values())>len(s[l:u+1]): s can have the dupes
            # while sum(d.values())>len([i for i in d if d[i]>0]):
            while s[u] in d:
                d.remove(s[l])
                l+=1
            d.add(s[u])
            res=max(res,u-l+1)
        return res
