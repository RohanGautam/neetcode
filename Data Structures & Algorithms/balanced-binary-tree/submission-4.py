# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Tuple, Optional
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def bal(node)->Tuple[Optional[int],bool]:
            if node is None:
                return (-1, True)
            if node.left is None and node.right is None:
                # return height of node and if it's valid
                return (0, True)
            
            left_res = bal(node.left)
            right_res = bal(node.right)
            if left_res[1] and right_res[1]:
                if abs(left_res[0]-right_res[0])<=1:
                    return (max(left_res[0], right_res[0])+1, True)
                else :
                    return (None, False)
            else:
                return (None, False)
        res = bal(root)
        return res[-1]