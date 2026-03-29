class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def isValid(s:str)->bool:
            stack = []
            for c in s:
                if c=="(":
                    stack.append(c)
                else:
                    if len(stack)>0:
                        stack.pop(c)
                    else:
                        return False
            return len(stack)==0

        res = []
        def bt(s="", oc=0,cc=0):
            if len(s)==2*n:
                res.append(s)
            
            if oc<n:
                bt(s+"(",oc+1,cc)
            if cc<oc:
                bt(s+")",oc,cc+1)
        bt()
        return res
 