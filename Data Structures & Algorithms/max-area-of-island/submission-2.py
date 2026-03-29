class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        maxArea=0
        rows, cols = len(grid), len(grid[0])


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1 and (i,j) not in seen:
                    # add visited nodes to seen
                    q = [(i,j)]
                    area=0
                    while len(q)!=0:
                        # this is O(N), can improve
                        # not pop(0), use like stack, dfs/bfs doesnt matter
                        cur = q.pop() 
                        seen.add(cur)
                        area+=1

                        n=[]
                        for delta_x,delta_y in [(1,0),(-1,0), (0,1),(0,-1)]:
                            i_new, j_new = cur[0]+delta_y, cur[1]+delta_x
                            if (0<=i_new<rows) and (0<=j_new<cols) and grid[i_new][j_new]==1 and ((i_new,j_new) not in seen):
                                n.append((i_new,j_new))
                                seen.add((i_new,j_new))

                        q.extend(n)
                    print(area)
                    maxArea = max(maxArea, area)
        return maxArea 