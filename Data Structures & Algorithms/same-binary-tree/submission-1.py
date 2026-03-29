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
        # elif (p is None and q is not None) or (q is None and p is not None):
        # will only be true if either are true, because of the check in the previous condition
        elif p is None or q is None:
            return False
        elif p.val!=q.val:
            return False

        # r = self.isSameTree(p.right, q.right)
        # l = self.isSameTree(p.left, q.left)
        # return r and l
        # this way if first is false, wont even compute the left
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        