class Solution:
    def distantSubarrays(self, nums: list[int], goal: int, k: int) -> int:
        n = len(nums)
        total = n * (n + 1) // 2

        if k == 0:
            return total
        
        lo = goal - k + 1
        hi = goal + k - 1

        sl = SortedList()
        prefix = 0
        sl.add(prefix)
        close = 0

        for num in nums:
            prefix += num
            left = prefix - hi
            right = prefix - lo
            close += sl.bisect_right(right) - sl.bisect_left(left)
            sl.add(prefix)

        return total - close
