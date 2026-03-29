class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={c:0 for c in set(s)}
        l=0
        maxlen = 0
        mostfreq = 0
        for u in range(len(s)):
            # increase frequency for current character
            d[s[u:u+1]]+=1
            # print(d)
            # get most frequent:
            # mostfreq = max(d.values())
            mostfreq = max(mostfreq, d[s[u:u+1]])
            if (u-l+1)-mostfreq <= k:
                # it's valid, keep track of max len
                maxlen=max(maxlen, u-l+1)
            else:
                # update lower pointer until it's valid
                while ((u-l+1)-mostfreq)>k:
                    # decrement the count in d
                    d[s[l:l+1]]-=1
                    # THEN move it forward
                    l+=1
        return maxlen