class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #  swap the most frequent character in each window :you get a limited number of swaps to ake the most of it
        # KEEP the most frequent character, the remaining can be candidates for the swap
        l = 0
        # you are moving the last pointer one forward to check for a longer one in each step
        res=0
        d={}
        for u in range(len(s)):
            d[s[u]] = d.get(s[u],0)+1
            most_freq = max(d.values())
            while len(s[l:u+1])-most_freq > k:
                d[s[l]]-=1
                l+=1
                most_freq = max(d.values())
            res = max(res, u+1-l)
        return res
            