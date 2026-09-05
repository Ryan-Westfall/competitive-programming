class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        leftDummy = ListNode(0)
        rightDummy = ListNode(0)

        left = leftDummy
        right = rightDummy

        cur = head

        while cur:
            if cur.val < x:
                left.next = cur
                left = left.next
            else:
                right.next = cur
                right = right.next

            cur = cur.next

        # Important: cut old links
        right.next = None

        # Connect the two lists
        left.next = rightDummy.next

        return leftDummy.next