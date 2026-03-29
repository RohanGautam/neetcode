class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # definitely a stack based approach
        # flip the script - instead of looking ot the future, think that 
        # for which past ones am i the max temp
        # strictly increasing stack? pop increase count
        result = [0 for _ in temps]
        s=[]
        for i in range(len(temps)):
            while s and temps[s[-1]]<temps[i]:
                pidx=s.pop()
                result[pidx]+=(i-pidx)
            s.append(i)
        return result
        