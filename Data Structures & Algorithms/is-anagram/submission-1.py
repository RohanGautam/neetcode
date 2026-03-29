class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        # for a,b in zip(sorted(list(s)), sorted(list(t))):
        #     if a!=b:
        #         return False
        # return True

        # not correct because two pairs of characters can be diff but have the same sum
        # return sum(map(ord,s)) == sum(map(ord,t))


        # or just maintain frequencies -> it's O(1) because atmost 26 characters (fixed)
        # or you can use a hash table [indices are used to update counts]
        d1,d2={},{}
        for e in s:
            if e not in d1:
                d1[e]=0
            d1[e]+=1

        for e in t:
            if e not in d2:
                d2[e]=0
            d2[e]+=1
        return d1==d2
