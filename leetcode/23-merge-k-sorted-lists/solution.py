class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists:
            return None

        def mergeList(nodeL, nodeR):
            dummy = ListNode()
            tail = dummy

            while nodeL and nodeR:
                if nodeL.val <= nodeR.val:
                    tail.next = nodeL
                    nodeL = nodeL.next
                else:
                    tail.next = nodeR
                    nodeR = nodeR.next

                tail = tail.next

            if nodeL:
                tail.next = nodeL
            else:
                tail.next = nodeR

            return dummy.next


        def combine(l, r):
            if l == r:
                return lists[l]

            mid = (l + r) // 2

            left = combine(l, mid)
            right = combine(mid + 1, r)

            return mergeList(left, right)

        return combine(0, len(lists)-1)