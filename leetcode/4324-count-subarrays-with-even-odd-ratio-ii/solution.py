class Solution:
    def countRatioSubarrays(self, A: list[int], a: int, b: int) -> int:
        s = SortedList([0])
        res = pre = 0
        for x in A:
            pre += a if x % 2 else -b
            res += s.bisect_right(pre)
            s.add(pre)
        return res