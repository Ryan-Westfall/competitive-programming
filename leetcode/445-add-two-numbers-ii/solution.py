# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        def reverse(head):
            prev = None
            while head:
                nxt = head.next
                head.next = prev
                prev = head
                head = nxt
            return prev

        l1 = reverse(l1)
        l2 = reverse(l2)

        carry = 0
        ans = None

        # Add while both lists have nodes.
        while l1 and l2:
            total = l1.val + l2.val + carry
            ans = ListNode(total % 10, ans)
            carry = total // 10
            l1 = l1.next
            l2 = l2.next

        # Reuse whichever list is longer.
        remaining = l1 if l1 else l2

        while remaining:
            total = remaining.val + carry
            remaining.val = total % 10
            carry = total // 10

            nxt = remaining.next
            remaining.next = ans
            ans = remaining
            remaining = nxt

        if carry:
            ans = ListNode(carry, ans)

        return ans