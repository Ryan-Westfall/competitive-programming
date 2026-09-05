class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hare = head
        turtle = head

        # Find meeting point
        while hare and hare.next:
            hare = hare.next.next
            turtle = turtle.next

            if hare == turtle:
                break
        else:
            return None

        # Find cycle entry
        hare = head
        while hare != turtle:
            hare = hare.next
            turtle = turtle.next

        return hare