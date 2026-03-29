class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # of course, we could reshape/flatten this and do 
        # a normal binary search for desired time. but that would 
        # occupy space. a more clever thing would be to just 
        # manipulate some pointers to keep track of stuff.
        m,n = len(matrix), len(matrix[0])

        # def ij2k(i,j):
        #     # m is rowns, n is cols
        #     # i is row idx, j is col idx
        #     return i*n+j
        def k2ij(k):
            return k//n, k%n


        l,h = 0, m*n-1
        while l<=h:
            m = l+((h-l)//2)
            i,j=k2ij(m)
            if target>matrix[i][j]:
                l=m+1
            elif target<matrix[i][j]:
                h=m-1
            else:
                return True
        return False
        