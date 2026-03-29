import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = "+-*/"
        num_stack=[]
        while len(tokens)>0:
            a = tokens.pop(0)
            if a in ops:
                v1,v2 = num_stack.pop(),num_stack.pop()
                print(a,v2,v1)

                if a=="+":
                    res = v1+v2
                elif a=="-":
                    res = v2-v1
                elif a=="*":
                    res = v1*v2
                elif a=="/":
                    if v1>=0 and v2>=0:
                        res = math.floor(v2/v1)
                    else:
                        res = math.ceil(v2/v1)

                num_stack.append(res)
            else:
                num_stack.append(int(a))
                
        return num_stack[0]
