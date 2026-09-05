class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        # Find length
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # Move to split point
        leftSideLength = math.ceil(length / 2)
        cur = head
        prev = None
        while leftSideLength:
            prev = cur
            cur = cur.next
            leftSideLength -= 1

        # Split the list
        prev.next = None

        # Reverse second half
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # Merge the two halves
        leftCur = head
        rightCur = prev

        while rightCur:
            leftNext = leftCur.next
            rightNext = rightCur.next

            leftCur.next = rightCur
            rightCur.next = leftNext

            leftCur = leftNext
            rightCur = rightNext