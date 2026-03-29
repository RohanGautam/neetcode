
from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nrow, ncol = len(grid), len(grid[0])
        seen = set()
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j]==0:
                    seen.add((i,j))
        
        q = deque([(v,0) for v in seen])
        while len(q)>0:
            cur,level = q.popleft()
            grid[cur[0]][cur[1]]=level
            
            for v in [(0,1),(0,-1),(1,0),(-1,0)]:
                ihat, jhat = cur[0]+v[0],cur[1]+v[1]
                # seen check here. if seen before, has been visited by a shorter route!
                if 0<=ihat<nrow and 0<=jhat<ncol and grid[ihat][jhat]!=-1 and (ihat,jhat) not in seen:
                    seen.add((ihat,jhat))
                    q.append(((ihat,jhat),level+1))


        