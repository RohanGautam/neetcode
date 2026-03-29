# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        s,f=head,head.next
        while f and f.next: # slick way for fast pointers
            s=s.next
            f = f.next.next
        print(s.val)
        # reverse from the middle onwards
        # not including the middle
        cur=s.next
        # terminate first half
        s.next=None
        prev=None
        while cur:
            tmp = cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        
        # prev is the head of the second half
        a,b=head,prev
        while a and b:
            tmp1,tmp2 = a.next, b.next
            a.next=b
            b.next=tmp1
            a,b = tmp1,tmp2

