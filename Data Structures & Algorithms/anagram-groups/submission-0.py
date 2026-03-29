class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # d = {} 
        # for s in strs:
        #     ss = ''.join(sorted(s))
        #     if ss not in d:
        #         d[ss]=[]
        #     d[ss].append(s)
        # return list(d.values())

        d = {}
        for s in strs: # O(n)
            f = [0]*26
            for c in s: # O(m)
                f[ord(c)-ord('a')]+=1
            # use frequency as key in hash map to group
            # awkward in python as lists cant be keys(not hashable)
            # convert to tuple
            key = tuple(f)
            if key not in d:
                d[key]=[]
            d[key].append(s)

        return list(d.values())
            

        
        
