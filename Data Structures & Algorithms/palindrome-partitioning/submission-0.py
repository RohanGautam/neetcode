class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # imsunderstood
        def isPal(s):
            return s==s[::-1]
        
        result=[]
        path=[]
        def bt(cur):

            if cur==len(s):
                result.append(path.copy())
                return

            for j in range(cur,len(s)):
                if isPal(s[cur:j+1]):
                    path.append(s[cur:j+1])
                    bt(j+1) # check if remaining part is valid (all ITS substrings are valid)
                    path.pop()
        bt(0)
        return result

        