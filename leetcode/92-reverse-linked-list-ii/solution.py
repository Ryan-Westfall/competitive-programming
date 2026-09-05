# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'), head)

        prev = dummy
        cur = head
        for _ in range(left - 1):
            prev = cur
            cur = cur.next

        lastNode = prev
        lastNode.next = None
        reverseTail = cur
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        lastNode.next = prev
        reverseTail.next = cur
        return dummy.next


            