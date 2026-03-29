# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif (p is None and q is not None) or (q is None and p is not None):
            return False
        
        if p.val == q.val:
            r = self.isSameTree(p.right, q.right)
            l = self.isSameTree(p.left, q.left)
            if r and l :
                return True
            return False
        else:
            return False
        