# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def fn(node, path=None):
            nonlocal count
            if path is None:
                path=[]
            if node is None:
                return
            print(node.val,path)
            count+=int(all([n<=node.val for n in path]))
            path = path+[node.val]
            fn(node.left, path)
            fn(node.right, path)
        fn(root)
        return count

'''
Task: number of nodes s.t. for all n  in path(node, root); n.val<=node.val
- traversal style might not matter as long as paths are formed and compared
- path from node to root is unique - only one path to consider

- st_1: Keep track of path leading up to current node, and at each node, see if all the values are lesser than the current in a loop
-> can we not track the whole path? maybe just pass along the max seen so far?
That wouldnt work because one element would dominate



'''