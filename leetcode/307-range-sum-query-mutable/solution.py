class SegmentTree:
    def __init__(self, nums):
        self.nums = nums
        self.tree = [0] * (len(nums) * 4)
        
    def build(self, node, nodeL, nodeR):
        if nodeL == nodeR:
            self.tree[node] = self.nums[nodeL]
            return self.nums[nodeL]

        mid = (nodeL + nodeR) // 2
        left = self.build(2 * node, nodeL, mid)
        right = self.build(2 * node + 1, mid + 1, nodeR)
        summation = left + right

        self.tree[node] = summation
        return summation

    def query(self, node, nodeL, nodeR, l, r):
        if nodeL >= l  and nodeR <= r:
            return self.tree[node]

        if l > nodeR or nodeL > r:
            return 0

        mid = (nodeL + nodeR) // 2
        left = self.query(node * 2, nodeL, mid, l, r)
        right = self.query(node * 2 + 1, mid + 1, nodeR, l, r)
        return left + right

    def update(self, node, nodeL, nodeR, index, newValue):
        if nodeL == nodeR:
            self.tree[node] = newValue
            self.nums[index] = newValue
            return

        mid = (nodeL + nodeR) // 2
        if index >= nodeL and index <= mid:
            self.update(node * 2, nodeL, mid, index, newValue)
        else:
            self.update(node * 2 + 1, mid + 1, nodeR, index, newValue)

        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]


class NumArray:

    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums)
        self.st.build(1, 0, len(nums) - 1)
        self.n = len(nums)
        
    def update(self, index: int, val: int) -> None:
        return self.st.update(1, 0, self.n - 1, index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query(1, 0, self.n - 1, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)