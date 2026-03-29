# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        rev_next = None
        while cur!=None:
            cur_next=cur.next
            cur.next=rev_next
            rev_next=cur
            cur=cur_next
        return rev_next
