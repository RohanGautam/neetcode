# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, po: List[int], io: List[int]) -> Optional[TreeNode]:
        
        # returns a treenode
        def fn(po,io):
            if len(po)==0:
                return None
            if len(po)==1:
                return TreeNode(po[0])
            print(po,io)
            root = po[0]
            node = TreeNode(root)
            # everything to the right of this in io is the right subtree, left is left subtree
            root_idx = io.index(root)
            num_left = root_idx
            node.left = fn(po[1:num_left+1], io[:root_idx])
            node.right = fn(po[num_left+1:],io[root_idx+1:])
            return node
        return fn(po,io)
            






'''
Rebuild using prerder and inorder traversal. The lists dont have null/None to indicate which side (that would be the answer)

- inorder is left->cur->right # io
- preorder is cur->left->right # po
- => unique values on the node

observations :
- root is po[0]
- p[1]-> root.left, or root.right (if left doesnt exist)
- can we tell if it doesnt exist based on io?
- if io[0]==p[1] then p[1] is root.left
- case: node had both right and left
    - io=[l,c,r], po=[c,l,r] => check and verify this
- case : node has only left
    - io=[l,c], po=[c,l]
- case: node has only right
    - io=[c,r], po=[c,r]
- case: node is a leaf
    - 
- ofc, each of these can be their own subtree, not individual nodes so not like they'd line up
- io[0] is the deepest, leftmost node

- how do we construct the tree- top down or bottom up?
- a current node we consider. initially this can be the root. we'll have to search it's index in the io list.
- 

tldr : have to search in io, for knowing how many on the left subtree and how many on the right

'''