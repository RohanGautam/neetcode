class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       # the flattened, row concatenated matrix is sorted basically
        r,c = len(matrix), len(matrix[0])
        l,h = 0, r*c-1
        while l<=h:
            m = l + ((h-l)//2)
            if matrix[m//c][m%c]<target:
                l=m+1
            elif matrix[m//c][m%c]>target:
                h=m-1
            else:
                return True
        return False