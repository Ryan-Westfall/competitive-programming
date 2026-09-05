# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carryover = 0
        dummy = prev = ListNode(0)
        while l1 or l2 or carryover == 1:
            curr = ListNode(0)
            if prev:
                prev.next = curr
            if l1:
                curr.val += l1.val
                l1 = l1.next
            if l2:
                curr.val += l2.val
                l2 = l2.next
            curr.val += carryover

            if curr.val >= 10:
                curr.val = curr.val % 10
                carryover = 1
            else:
                carryover = 0
            prev = curr
            
        return dummy.next
        
            