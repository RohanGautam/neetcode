class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # maintain char:frequency
        d={}
        l=0
        res = 0
        for u in range(len(s)):
            d[s[u]] = d.get(s[u],0)+1
            # while sum(d.values())>len(s[l:u+1]): s can have the dupes
            while sum(d.values())>len([i for i in d if d[i]>0]):
                d[s[l]]-=1
                l+=1
            res=max(res,u-l+1)
        return res
