class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        digits='123456789'
        for i in range(9):
            row_buf,col_buf,sq_buf=[],[],[]
            for j in range(9):
                row_val=board[i][j]
                col_val=board[j][i]
                sq_val=board[j//3 + (i//3)*3][j%3 + (i%3)*3]

                if row_val in digits:
                    if row_val in row_buf:
                        return False
                    row_buf.append(row_val)
                if col_val in digits:
                    if col_val in col_buf:
                        return False
                    col_buf.append(col_val)
                
                if sq_val in digits:
                    if sq_val in sq_buf:
                        return False
                    sq_buf.append(sq_val)
        return True

        