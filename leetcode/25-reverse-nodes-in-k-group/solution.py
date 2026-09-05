# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            # Find the kth node from groupPrev
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            groupNext = kth.next

            # Reverse this group
            prev = groupNext
            cur = groupPrev.next

            while cur != groupNext:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            # Reconnect the reversed group
            oldHead = groupPrev.next   # becomes the tail
            groupPrev.next = kth       # kth is now the head
            groupPrev = oldHead        # move to next group