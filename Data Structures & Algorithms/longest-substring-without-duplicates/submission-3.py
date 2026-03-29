class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        # elif len(s)==1:
            # return 1
        else:
            # seen=set()
            # # l,u=0,1
            # total = 0
            # for c in s:
            #     if c not in seen:
            #         seen.add(c)
            #         total=max(total,len(seen))
            #     else:
            #         # resetting does not work
            #         seen=set([c])
            # return total
            d={}
            total = 0
            for i,c in enumerate(s):
                if c not in d:
                    d[c]=i
                else:
                    # keep track of the total seen so far
                    total=max(total,len(d))                    
                    prev_idx = d[c]
                    # remove that and prev idx ones
                    # this part touches each caracter only once in total, so it's 
                    # not O(n^2)
                    to_remove = [k for k in d.keys() if d[k]<prev_idx]
                    for k in to_remove:
                        d.pop(k)
                    # overwrite cur idx
                    d[c]=i
            total=max(total,len(d))
            return total