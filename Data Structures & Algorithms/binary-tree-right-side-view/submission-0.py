# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node, level):
            if node is None:
                return
            # will not be true if you already saw something at that level
            # executed once per level!
            if level+1>len(res):
                # only place where node can be added
                res.append(node.val)
            dfs(node.right, level+1) # right first
            dfs(node.left, level+1) 
        dfs(root,0)
        return res
            


# task: return nodes visible only from the right side. - no path between a ray originating from the right and to that node.
# st_1: taking all the right nodes -> doesnt work because subnodes might not be _rightmost_.
# We want, at each level, the rightmost nodes. result = list of len(level of the tree)
# st_2 : do a BFS and store nodes in a level (level order traversal) 
#      - take the last element from the list of lists as the answer
#      - this would definitely work
# Is there a way that does not involve materialising the whole tree?
# st_3: do a DFS that goes as right as possible. if not, goes left, ignoring elements if something else was seen at that level already
#      - consider example 2
#      - dfs(1) -> note level 1:[1] dfs(1.right=3) and dfs(1.left=4)
#      - dfs(3) -> {1:1, 2:3} (level-element seen map) -> dfs(none) and dfs(none)
#      - dfs(4) -> level2 already in map! -> dont update -> dfs(4.right) and dfs(4.left)
#      - ... adds 4 and 5 -> {1:1,2:3,3:4,4:5}