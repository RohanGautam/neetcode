# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maximum=0
    def db(self, root: Optional[TreeNode]) -> int:
        # longest = longest from right + longest from left of each node.
        if root is None:
            return -1
        l = self.db(root.left)+1
        r = self.db(root.right)+1
        self.maximum=max(self.maximum, l+r)
        # need to return just the max height to the parent,
        # but keep track of the sum in case it's the maximum
        # print(root.val, l,r, l+r)
        return max(l,r)
    def diameterOfBinaryTree(self, root: Optional[TreeNode],m=0) -> int:
        self.db(root)
        return self.maximum
