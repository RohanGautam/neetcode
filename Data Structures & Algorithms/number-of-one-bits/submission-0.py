class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        for i in range(32):
            shifted = 1<<i
            c+=int((n&shifted)==shifted)
        return c


'''
The number of 1's in it's binary representation 
If we're thinking bit manipulation let's look at our options:
- shifts : wont work because this requires aggregation
- or, and : all bitwise - how will information be aggregated

so we loop, check each position that n&(1<<idx (0->n-1))==1<<idsx
'''