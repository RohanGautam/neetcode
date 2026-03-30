# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = l1
        carry=0
        # case 2
        while l1 or l2:
            if l1 and l2:
                total = l1.val+l2.val+carry
                l1.val, carry = total%10, total//10
                end=l1
                l1,l2 = l1.next, l2.next
            elif l1:
                total = l1.val+carry
                l1.val, carry = total%10, total//10
                end=l1
                l1=l1.next
            elif l2:
                # l1 is now the rest of l2
                end.next=l2
                l1=l2
                l2=None # work on l1 in the next iteration
        if carry:
            end.next=ListNode(carry,None)
        return head

'''
Add two numbers, where each of the ten's place is stored in a different LL node. The head is the first digit (0th place)
The result should also be a linked list.

This seems more of a procedural reasoning test.
if we have both nodes not none, then we can modify either one in place to represent the solution, and have a carry variable for the rest. 

case 1: both are exactly the same length and dont exceed over 9 in each spot
    - in this case, we just update one of the lists and move on
case 2: same as above but overflow allowed.
    - have a carry variable. if carry remains at end, add as a new node.
case 3: different length eg:(1+99999)
    - if reach a none and the other isn't then add the remaining digits to the solution and just propagate the carry
'''
     