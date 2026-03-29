# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        s=[root]
        cur=s[0]
        count=0
        while s:
            # pop ponly after going as left as you can
            while cur:
                s.append(cur)
                cur=cur.left
            cur = s.pop()
            count+=1
            if count==k:
                return cur.val
            cur=cur.right