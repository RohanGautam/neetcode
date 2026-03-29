class MinStack:
    # key idea: everything is O(1) except the getmin (naive)
    # so we can use another stack that alwasy has the minimum

    def __init__(self):
        self.s=[]
        self.m=[]        

    def push(self, val: int) -> None:
        self.s.append(val)
        if len(self.m)==0:
            self.m.append(val)
        else:
            self.m.append(min(self.m[-1],val))
        

    def pop(self) -> None:
        self.s.pop()
        self.m.pop()
        

    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.m[-1]
        
