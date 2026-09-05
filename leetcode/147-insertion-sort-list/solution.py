# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-9999, head)
        orderPointer = head
        prevOrderPointer = dummyHead
        while orderPointer:
            if orderPointer.val < prevOrderPointer.val:
                # Fix out of order pointers
                prevOrderPointer.next = orderPointer.next

                insertPointer = dummyHead.next
                prevInsertPointer = dummyHead
                while insertPointer:
                    if orderPointer.val < insertPointer.val:
                        prevInsertPointer.next = orderPointer
                        orderPointer.next = insertPointer
                        break

                    prevInsertPointer = prevInsertPointer.next
                    insertPointer = prevInsertPointer.next

            if prevOrderPointer.next == orderPointer:
                prevOrderPointer = prevOrderPointer.next

            orderPointer = prevOrderPointer.next

        return dummyHead.next

                
