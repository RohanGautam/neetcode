# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # add a .prev attribute for easier downstream cycling
        cur=head
        prev=None
        last=None
        c=0
        while cur is not None:
            cur.prev = prev
            cur.idx=c
            prev = cur
            if cur.next is None:
                print(cur.val)
                last=cur
            cur = cur.next
            c+=1
        # print(head.val, last.val)
        cur=head
        n,p = cur.next,last.prev
        while cur.idx<=last.idx:
            # if adjacent (even)
            if cur.next == last:
                last.next = None
                break
            n,p = cur.next,last.prev
            cur.next = last
            last.next=n
            cur=n
            last=p
            # if equal (odd)
            if cur==last:
                if cur:
                    cur.next=None
                break

        # n.next=None
        # return head
