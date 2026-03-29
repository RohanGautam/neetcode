class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        path = set()
        def bt(i,j,pos):
            if pos==len(word):
                return True
            

            if not (0<=i<len(board) and 0<=j<len(board[0]) and (i,j) not in path and  word[pos]==board[i][j]):
                return False
            
            tmp = board[i][j]
            # mark current pos as seen. continue searching from there and undo it so other paths can use it too
            path.add((i,j))
            
            res = bt(i+1,j,pos+1) or bt(i-1,j,pos+1) or bt(i,j+1,pos+1) or bt(i,j-1,pos+1)
            # undo having seen that in this path . we reach here if all of the above or-called chains are False
            # if this was not the root, you'd continue from somewhere else, and having this removed from seen means this can be a part of those paths
            path.remove((i,j))
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==word[0] and bt(i,j,0):
                    return True
        return False 