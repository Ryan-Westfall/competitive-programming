class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        count = 0
        cur = head
        while cur:
            cur = cur.next
            count += 1

        k %= count
        if k == 0:
            return head

        # Walk to the node BEFORE the new head
        steps = count - k - 1
        cur = head
        for _ in range(steps):
            cur = cur.next

        newHead = cur.next
        cur.next = None

        tail = newHead
        while tail.next:
            tail = tail.next

        tail.next = head

        return newHead