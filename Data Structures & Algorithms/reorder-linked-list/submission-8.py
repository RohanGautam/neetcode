# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        # basically, we have to reverse the second half, then make connections from the first and second in an alternating way.
        # fast and slow to find the middle
        f,s = head.next,head
        while f and f.next:
            s=s.next
            f = f.next.next
        # s is now the middle node, and f will terminate when it reaches None.
        # reverse the middle part after cutting ties with the first part
        # we can actually - start reversing from middle +1 - will result in no changes actually
        cur = s.next
        s.next=None # cut off first half
        print(s.val, cur.val)
        # reverse LL starting from middle
        prev = None
        while cur: # made mistake
            tmp = cur.next
            cur.next=prev
            prev=cur
            cur=tmp
        # cur is now the head of the reversed linked list
        # we now just have to alternate between the nodes of the lists
        # print(cur.val, cur.next.val)
        h1,h2 = head,prev
        while h2:
            tmp1, tmp2 = h1.next, h2.next
            h1.next = h2
            h2.next=tmp1
            h1 = tmp1
            h2=tmp2

