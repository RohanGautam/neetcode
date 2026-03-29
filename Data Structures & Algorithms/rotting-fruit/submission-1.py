from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # max time would be the max distance to the closest rotten fruit

        nrows,ncols=len(grid),len(grid[0])
        seen = set()
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j]==2:
                    seen.add((i,j))
        q=deque([(v,0) for v in list(seen)])
        maxval = 0
        while len(q)>0:
            cur,level = q.popleft()
            # this element not seen, level = prev level+1
            grid[cur[0]][cur[1]]=2
            maxval=max(maxval,level)
            # add neighbours to the stack
            for v in [(1,0),(-1,0),(0,1),(0,-1)]:
                ihat,jhat = cur[0]+v[0], cur[1]+v[1]
                if 0<=ihat<nrows and 0<=jhat<ncols and grid[ihat][jhat]!=0 and (ihat,jhat) not in seen:
                    seen.add((ihat,jhat))
                    q.append(((ihat,jhat),level+1))
        # check if any fresh remaining
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j]==1:
                    return -1
        return maxval
            