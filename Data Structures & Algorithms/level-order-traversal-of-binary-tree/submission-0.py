# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
            
        q = deque([(root,0)])
        res=[]
        while len(q)>0:
            node,level = q.popleft()
            if level+1>len(res):
                res.append([])
            res[level].append(node.val)
            if node.left:
                q.append((node.left,level+1))
            if node.right:
                q.append((node.right,level+1))
            
        return res

# we want the level order traversal - each level should be in it's own list
# propagate a level number through
# just bfs though, with levels propagated.
# have a level:list mapping that you can use to append to, but even that is not needed
# can check if level is out of bounds to the list of lists before adding
# Example : example 1 in the problem statement
# q = [(1,0)] -> 1>0 => res=[[]]->[[1]] -> q=[(2,1),(3,1)]
# q=[(2,1)] (after pop) - 2>1->res=[[1],[2]] -> [[1],[2,3]]
