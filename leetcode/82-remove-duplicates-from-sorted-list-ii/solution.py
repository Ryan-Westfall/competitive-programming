# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float("-inf"), head)

        lastDistinct = dummy
        cur = head

        while cur:
            prev = cur
            cur = cur.next

            # prev was unique
            if not cur or prev.val != cur.val:
                lastDistinct.next = prev
                lastDistinct = prev
            else:
                # Skip every duplicate
                while cur and cur.val == prev.val:
                    cur = cur.next

                # Remove the duplicate block
                lastDistinct.next = cur

        # Cut off any remaining duplicate nodes
        lastDistinct.next = None

        return dummy.next