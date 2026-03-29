class TimeMap:

    def __init__(self):
        self.d={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key]=[]
        # timestamps are in strictly increasing order! hint for binary search
        self.d[key].append((timestamp,value))        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.d:
            return ""
        l,u = 0,len(self.d[key])-1
        valid_idx = None
        while l<=u:
            m = l+ (u-l)//2
            if self.d[key][m][0]<=timestamp:
                if valid_idx is None:
                    valid_idx=m
                else:
                    if self.d[key][m][0]>=self.d[key][valid_idx][0]:
                        valid_idx=m
                l=m+1
            elif self.d[key][m][0]>timestamp:
                u=m-1
        if valid_idx is None:
            return ""
        else:
            return self.d[key][valid_idx][1]
        
        
