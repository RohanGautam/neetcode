class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        # def isValid(s:str)->bool:
        # cant even use this because need to check full length set to see if its valid. cant do in a bit by bit way
        #     stack = []
        #     for c in s:
        #         if c=="(":
        #             stack.append(c)
        #         else:
        #             if len(stack)>0:
        #                 stack.pop(c)
        #             else:
        #                 return False
        #     return len(stack)==0

        res = []
        # [] in arg is a mutable reference by default
        def bt(path=[], oc=0,cc=0):
            if len(path)==2*n:
                # "backs up" to try other branches when a path is finished.
                # that's what makes this backtracking
                res.append(''.join(path))
            
            if oc<n:
                path.append("(")
                bt(path,oc+1,cc)
                path.pop()
            if cc<oc:
                path.append(")")
                bt(path,oc,cc+1)
                path.pop()
        bt()
        return res
 