# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        output = []

        cur = head
        index = 0
        while cur:
            output.append(0)
            while stack and cur.val > stack[-1][0]:
                _, stackIndex = stack.pop()
                output[stackIndex] = cur.val
            stack.append((cur.val, index))
            cur = cur.next
            index += 1

        return output
        