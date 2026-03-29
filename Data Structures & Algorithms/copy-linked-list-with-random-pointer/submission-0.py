"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d={None:None}
        def dfs(node):
            if node in d:
                return d[node]
            d[node] = Node(node.val, dfs(node.next),node.random)
            return d[node]
        head = dfs(head)
        cur = head
        print(d)
        while cur is not None:
            cur.random=d[cur.random]
            cur=cur.next
        return head
            


'''
in this problem, we have to copy the linked list as well as the random nodes.
lets first assume there is no random pointer. 

dfs will naturally materialise the end of the linked list first, we can use this to recursively create deep copies.

now for the random pointer, we can just look it up from a hashmap (memoised dfs)
but that can cause infinite loops.
maybe we first materialise the noemal linked list in O(N), then use O(N) extra space to have a old->new lookup table
Then we can use the looup table to update the random pointer
'''