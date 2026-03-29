class MinStack:
    # key idea: everything is O(1) except the getmin (naive)
    # so we can use another stack that alwasy has the minimum
    # the slick way can actually use only one stack.
    # we store the differences

    def __init__(self):
        self.s=[]
        # can use number instead of list
        self.m=float('inf')        

    def push(self, val: int) -> None:
        # want negative if there is a change in min
        if len(self.s)==0:
            self.s.append(0)
            self.m=val
        # self.s.append(val-self.m)
        else:
            self.s.append(val-self.m)
            self.m = min(self.m,val)


        # if len(self.s)==0:
        #     self.m=v
        #     self.s.append(val)
        # if len(self.m)==0:
        #     self.m.append(val)
        # else:
        #     self.m.append(min(self.m[-1],val))
        

    def pop(self) -> None:
        v = self.s.pop()
        if v<0:
            # need to update min too
            self.m = self.m-v # add it
        # self.m.pop()
        

    def top(self) -> int:
        if self.s[-1]>0:
            # during push, min stayed the same
            return self.s[-1]+self.m
        else:
            # min was updated and the last val was set to m
            return self.m
        

    def getMin(self) -> int:
        return self.m
        
