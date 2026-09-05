# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def splitMerge(node):
            if not node:
                return
            if not node.next:
                return node

            slow = node
            fast = node
            prev = None
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next

            prev.next = None

            if node == slow:
                return node

            left = splitMerge(node)
            right = splitMerge(slow)

            return merge(left, right)

        def merge(leftList, rightList):
            dummyNode = ListNode(float('-inf'), None)
            cur = dummyNode
            while leftList and rightList:
                if leftList.val < rightList.val:
                    cur.next = leftList
                    leftList = leftList.next
                    cur = cur.next
                else:
                    cur.next = rightList
                    rightList = rightList.next
                    cur = cur.next


            if leftList:
                cur.next = leftList
            else:
                cur.next = rightList

            return dummyNode.next
        
        return splitMerge(head)