# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def fn(node, cur_max=float('-inf')):
            nonlocal count
            if node is None:
                return
            count+=int(cur_max<=node.val)
            cur_max = max(cur_max, node.val)
            fn(node.left, cur_max)
            fn(node.right, cur_max)
        fn(root)
        return count

'''
Task: number of nodes s.t. for all n  in path(node, root); n.val<=node.val
- traversal style might not matter as long as paths are formed and compared
- path from node to root is unique - only one path to consider

- st_1: Keep track of path leading up to current node, and at each node, see if all the values are lesser than the current in a loop
-> can we not track the whole path? maybe just pass along the max seen so far?
That wouldnt work because one element would dominate
wait actually let's revisit this
-> 2->1->3 (2->2->3) # actually this works, no?

-> what about passing minimums?but that would mean there's possible a bigger violating maximum
-> ler's revisit the maximum -> any one value bigger makes it invalid. 


'''