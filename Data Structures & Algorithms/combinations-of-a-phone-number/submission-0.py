class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        d={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        
        res = []
        path = []
        def bt(pos):
            if pos==len(digits):
               res.append(''.join(path)) 
               return
            
            for c in d[int(digits[pos])]:
                path.append(c)
                bt(pos+1)
                # to give other characters at this level a chance
                path.pop()
        bt(0)
        return res
            

'''
Observations
- say we have d: digits->chars; if n digits, # combinations = product of # of chars per digit
- 2<=d<=9 -> 1 doesnt map to a character.


'''