from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        n = len(nums1)
        if n == 1:
            return True

        m = min(nums1)
        if m % 2 == 1:
            return True

        for x in nums1:
            if x % 2 == 1:
                return False
        return True