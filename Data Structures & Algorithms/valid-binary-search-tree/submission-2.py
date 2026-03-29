# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return both max and the min
        def fn(node):
            if node is None:
                # valid, min, max
                return True, float('inf'), float('-inf')
            
            cond = True
            cur_maxval = node.val
            cur_minval = node.val

            if node.right:
                is_valid, minval, maxval = fn(node.right)
                cond = cond and is_valid and minval>node.val
                cur_maxval = max(cur_maxval,maxval)
                cur_minval = min(cur_minval,minval)

            if node.left:
                is_valid, minval, maxval = fn(node.left)
                cond = cond and is_valid and maxval<node.val
                cur_maxval = max(cur_maxval,maxval)
                cur_minval = min(cur_minval,minval)
            return cond, cur_minval, cur_maxval
        return fn(root)[0]

'''
st_1: for a node:
    - right to be valid
    - left to be valid
    - values in the right order (right<cur<left)

      5
    1   4
       3  6
---
return valid, min, max
5->1->True, 1, 1
 ->4 
    ->3 -> True, 3,3
    ->6 -> True, 6, 6
    => left: max seen so far is lesser than current -> 3<4 -> yes
    => right: min seen so far is more than current -> 6>4 -> yes
    => actually, this form all is_valid logic, we dont need to pass a boolean
    => stick with it for this version

Correction: All subtrees must follow that order too - every value in subtree must have that order too, left subtree any val cant exceed the right
st_2: keep track of the maximum left and right values. the check should be done with these, instead of just node values

correction number 2- it's the maximum on the left side and the minimum on the right side
'''
        