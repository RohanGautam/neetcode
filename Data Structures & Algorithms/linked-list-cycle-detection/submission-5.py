# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False
        cur=head
        s,f=cur,cur.next.next
        while f and s:
            if f==s:
                return True
            s=s.next #jump once
            if f.next is None:
                return False
            f=f.next.next #jump twice
        return False