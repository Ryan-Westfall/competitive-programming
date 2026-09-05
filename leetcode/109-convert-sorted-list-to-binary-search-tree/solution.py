# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def splitList(node):
            fast = node
            slow = node
            prev = None
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
                
            prev.next = None
            return slow


        def dfs(linkedListNode):
            if not linkedListNode:
                return None

            if not linkedListNode.next:
                return TreeNode(linkedListNode.val)

            middle = splitList(linkedListNode)
            left = dfs(linkedListNode)
            right = dfs(middle.next)

            return TreeNode(middle.val, left, right)


        return dfs(head)


        