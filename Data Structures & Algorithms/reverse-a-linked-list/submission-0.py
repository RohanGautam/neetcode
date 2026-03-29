# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        cur=head
        new_next=None
        head=True

        while True:
            # keep track of the next one
            next = cur.next
            # overwrite the current next with a new next
            cur.next=new_next
            new_next=cur
            if next is None:
                break
            cur=next
        return cur

            
