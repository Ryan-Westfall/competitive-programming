# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next

        self.n = n - 1
        

    def getRandom(self) -> int:
        nodeNum = randint(0, self.n)

        cur = self.head
        while nodeNum:
            cur = cur.next
            nodeNum -= 1

        return cur.val

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()