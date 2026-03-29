class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        l=[]
        for i in range(len(temps)):
            c=0
            maxflag=False
            for j in range(i+1,len(temps)):
                c+=1
                if temps[j]>temps[i]:
                    maxflag=True
                    break
            l.append(c if maxflag else 0)
        return l

        