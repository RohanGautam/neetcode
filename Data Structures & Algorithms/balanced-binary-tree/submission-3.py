# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if node is None:
                # trivial case
                return 0
            # left and right returning the heights of the left and right sides
            # has to be the complete height
            r = dfs(node.left)
            l = dfs(node.right)
            if r<0 or l<0:
                return -1
            h=max(r,l)+1
            print(node.val, r,l,h)

            if abs(r-l)>1:
                return -1
            return h # has to be for 

        out = dfs(root)
        if out>=0:
            return True
        return False
        
        
        