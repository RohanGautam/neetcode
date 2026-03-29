# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        cur=head
        while cur.next:
            if hasattr(cur,'visited'):
                return True
            else:
                cur.visited=True
                cur=cur.next
        return False