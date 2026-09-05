"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            cur = Node(insertVal)
            cur.next = cur
            return cur

        cur = head

        while cur.next != head:
            if cur.val <= insertVal <= cur.next.val:
                newNode = Node(insertVal, cur.next)
                cur.next = newNode
                return head
            elif cur.val > cur.next.val:
                if insertVal >= cur.val or insertVal <= cur.next.val:
                    newNode = Node(insertVal, cur.next)
                    cur.next = newNode
                    return head
            cur = cur.next

        newNode = Node(insertVal, cur.next)
        cur.next = newNode
        return head
        

        