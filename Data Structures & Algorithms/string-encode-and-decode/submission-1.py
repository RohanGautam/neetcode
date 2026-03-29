class Solution:

    def encode(self, strs: List[str]) -> str:
        # need an integer for length and another delimiter
        # the other deimiter helps us see where our number ends
        # since all info needs to be in the encoded string.
        res=''
        for s in strs:
            res += (str(len(s))+'>'+s)
        return res


    def decode(self, s: str) -> List[str]:
        # print(s)
        i=0
        num_str=''
        out = []
        while i<len(s):
            if s[i]=='>':
                # read out string
                n = int(num_str)
                out.append(s[i+1:i+1+n])
                i+=n+1
                num_str=''
            else:
                # buld num_str
                num_str+=s[i]
                i+=1
        return out
        
