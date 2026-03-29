# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        total=0
        while cur:
            total+=1
            cur=cur.next
        target = total-n
        if target==0:
            return head.next

        c=0
        cur,prev=head,None
        while cur:
            if c==target:
                prev.next=cur.next
                return head
            prev=cur
            cur=cur.next
            c+=1



'''
We have to remove the nth node from the end. from the start would be trivial, you just count up.

- st_1: traverse to count the total. then traverse again total-n times and perform a replacement.
    - this would be O(N+N)


'''