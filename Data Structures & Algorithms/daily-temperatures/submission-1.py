class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        s = []
        l = [0]*len(temps)
        for i in range(len(temps)):
            while len(s)>0 and temps[i]>temps[s[-1]]:
                pidx = s.pop()
                l[pidx] = i-pidx
            s.append(i)
        return l

        