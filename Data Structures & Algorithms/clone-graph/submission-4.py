"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# import copy
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        # In Python, custom objects (like your Node class) are hashable by default based on their memory address (identity), even if they contain unhashable attributes like a list of neighbors.
        old2new = {}
        def dfs(node):
            if node in old2new:
                return old2new[node]
            # set first so it doesnt infinitely cycle
            old2new[node] = Node(node.val)

            neighbors = [dfs(n) for n in node.neighbors]
            old2new[node].neighbors = neighbors
            return old2new[node]
        return dfs(node)