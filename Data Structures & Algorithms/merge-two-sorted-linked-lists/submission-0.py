# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # since we recieve an optional type, handle the cases
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        else:
            # both are not None
            c1,c2 = list1,list2
            res_head=None
            res_cur=None
            while (c1 is not None) and (c2 is not None):
                print(c1.val,c2.val)
                if c1.val<=c2.val:
                    if res_head is None:
                        res_head=c1
                        res_cur=res_head
                    else:
                        res_cur.next=c1
                        res_cur=res_cur.next
                    c1=c1.next
                else:
                    if res_head is None:
                        res_head=c2
                        res_cur=res_head
                    else:
                        res_cur.next=c2
                        res_cur=res_cur.next
                    c2=c2.next
            if c1:
                res_cur.next=c1
            if c2:
                res_cur.next=c2
            return res_head
                        

        


