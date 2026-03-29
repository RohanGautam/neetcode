class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # indices that i already saw
        seen = [] 
        count=0
        rows, cols = len(grid), len(grid[0])

        def neighbours(cur:tuple)->list[tuple]:
            '''gets a valid neighbour that you havent seen before'''
            i,j=cur
            n = []
            deltas = [(1,0),(-1,0), (0,1),(0,-1)]
            for delta_x,delta_y in deltas:
                i_new, j_new = i+delta_y, j+delta_x
                if (0<=i_new<rows) and (0<=j_new<cols) and grid[i_new][j_new]=='1' and ((i_new,j_new) not in seen):
                    n.append((i_new,j_new))
            return n

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1' and (i,j) not in seen:
                    print(i,j)
                    print(neighbours((i,j)))
                    count+=1
                    # do a bfs - why not dfs?
                    # add visited nodes to seen
                    q = [(i,j)]
                    while len(q)!=0:
                        # pop from start because BFS
                        cur = q.pop(0) 
                        seen.append(cur)
                        q.extend(neighbours(cur))
        return count





