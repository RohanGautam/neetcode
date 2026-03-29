# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode, history=[]) -> TreeNode:
        # - unique node vals, node can be a descendant of itself
        # p,q exist, p!=q

        phist = []
        qhist = []
        print(p.val, q.val)
        def dfs(node,h=None):
            nonlocal phist,qhist
            if node is None:
                return h 
            else:
                if h is None:
                    h=[]
                # dont want to modify in place
                h = h+[node]
                if node.val == p.val:
                    # print("here")
                    phist.extend(h)
                    # print(phist)
                if node.val==q.val:
                    qhist.extend(h)
                    # print(qhist)
                # either way, continue looking
                dfs(node.left,h)
                dfs(node.right,h)
        dfs(root)
        
            

        minlen = min(len(phist), len(qhist))
        # print([i.val for i in phist], [i.val for i in qhist])
        lca=root
        for i in range(minlen):
            if phist[i].val==qhist[i].val:
                lca=phist[i]
            else:
                break
        #     print(phist[minlen-i-1], qhist[minlen-i-1])
        #     if phist[minlen-i-1]==qhist[minlen-i-1]:
        #         return phist[minlen-i-1]
        return lca