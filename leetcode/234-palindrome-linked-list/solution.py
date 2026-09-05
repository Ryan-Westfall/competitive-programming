# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        fast, slow = head, head
        
        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
           
        secondHalfHead = self.reverse(slow)
        firstHalfHead = head
        
#         print(firstHalfHead)
#         print(secondHalfHead)
            
        while firstHalfHead and secondHalfHead:
            
            if(firstHalfHead.val != secondHalfHead.val):
                return False
            firstHalfHead = firstHalfHead.next
            secondHalfHead = secondHalfHead.next
        return True;
    
    def reverse(self,head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev

        