class MinStack:

    def __init__(self):
        self.m=[]
        self.s=[]
        

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
        # the trick is to figure out how to do this in O(1)
        # I think what we did was maintain a minimum list,
        # where the list had the minumum at every point there was a push.
        return self.m[-1]
        
