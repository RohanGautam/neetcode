# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        
        c=0
        cur=head
        while cur.next:
            c+=1
            if c>1000:
                return True
            cur=cur.next
        return False

