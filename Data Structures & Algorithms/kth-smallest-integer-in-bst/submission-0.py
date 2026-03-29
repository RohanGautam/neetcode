# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # returns the index in sorted array for the node
        # def fn(node, count=0):
        #     if node is None:
        #         return 0 # add nothing to the count
        #     count = fn(node.right)+1
        #     if count==k:
        #         return node.val
            
        #     return fn(node.left)

        # return fn(root)
        s= [root]
        expanded = set()
        c=0
        while s:
            print([x.val for x in s])
            cur = s.pop()
            if cur not in expanded:
                expanded.add(cur)
                if cur.right:
                    s.append(cur.right)
                s.append(cur)
                if cur.left:
                    s.append(cur.left)
            else:
                c+=1
                if c==k:
                    return cur.val
        return None
                



'''
- given a BST, return k'th smallest value.
- st_1 : dfs/bfs tree to construct a list, sort, and look at the k-1 index.
    - O(n) space, O(nlogn), doesn't make use of BST property.
- observation: smallest is deepest and leftmost, followed by it's parent, followed by by it's sibling
- st_2: do a dfs with order: left -> cur -> right (inorder). maintain a count. when count hits k, return the value
    - [2,1,3], k=2 
    - fn(2) -> fn(1)+1+fn(2) -> 1+1+1 -> 3
    - the left part does not depend on the parent's count, but the right part does
- st_3 : do a dfs (inorder traversal) with a stack. 
    - for a node n, pop it, add node.right,node,node.left to the stack until you cant anymore (you reach a leaf node. 
    - mark nodes as expanded when you expand them and add to the stack
    - [2,1,3]
    - s=[2],e=() => e=(2), s=[3,2,1] -> 1-> e=(1,2)s=[3,2,1] -> 1->c=1, check
'''
        