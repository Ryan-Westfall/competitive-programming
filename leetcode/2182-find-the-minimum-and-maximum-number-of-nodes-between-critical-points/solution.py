# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        output = [-1,-1]
        lastSeenIndex = None
        firstSeenIndex = None
        prev = None
        index = 0
        while cur.next:
            prev = cur
            cur = cur.next
            index += 1

            if cur.next and prev and (((cur.val > prev.val) and (cur.val > cur.next.val)) or ((cur.val < prev.val) and (cur.val < cur.next.val))):
                if lastSeenIndex:
                    output[0] = min(output[0], index - lastSeenIndex) if output[0] != -1 else index - lastSeenIndex
                    output[1] = index - firstSeenIndex
                
                if not firstSeenIndex:
                    firstSeenIndex = index

                lastSeenIndex = index

        return output






