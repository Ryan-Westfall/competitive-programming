# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        cur = head
        prev = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        cur = prev
        prev = None
        while cur and cur.val == 9:
            cur.val = 0
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        if not cur:
            head = ListNode(1, prev)
            return head

        cur.val += 1

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            

        return head


