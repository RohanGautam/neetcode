class Solution:
    def checkValidString(self, s: str) -> bool:
        # these represent upper and lower bounds on UNMATCHED OPEN brackets
        l,u=0,0
        for c in s:
            if c=='(':
                l+=1
                u+=1
            elif c==')':
                l = max(0, l-1 )
                u-=1
                if u<0:
                    return False
            else:
                # the * could be ( -> increasing the lower bound
                # could also be a closeed bracked - decreasing )
                # but be optimistic with *, so assume that it could be the best case - this is also true
                u+=1
                l= max(0, l-1)
        return l==0
