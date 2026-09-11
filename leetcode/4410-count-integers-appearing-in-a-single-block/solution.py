class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        lastSeen = {}
        bad = set()
        count = len(set(nums))

        for r, x in enumerate(nums):
            if x in bad:
                continue

            if x in lastSeen and r - lastSeen[x] > 1:
                count -= 1
                bad.add(x)

            lastSeen[x] = r

        return count