class Solution:
    def countBits(self, n: int) -> List[int]:
        return [str(bin(i)).count('1') for i in range(n+1)]
'''
maybe we decompose into powers of two

2^1 - 1


'''