class MinStack:

    def __init__(self):
        self.l=[]
        self.p=[]
        self.m = float("inf")
        

    def push(self, val: int) -> None:
        self.l.append(val)
        # track the current minimum
        if val<self.m:
            self.m=val

        self.p.append(self.m)
        
    def pop(self) -> None:
        self.l.pop()
        self.p.pop()
        # note : also to update the current minimum 
        # when the minima list is updated,
        # for when we will possible subsequently push after this operation.
        self.m=self.p[-1] if self.p else float('inf')
        

    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:
        return self.p[-1]
        
