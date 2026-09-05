class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        lastSeenIndex = None
        seen = set()

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] not in seen:
                seen.add(nums[i])
            else:
                lastSeenIndex = i
                break

        return math.ceil((lastSeenIndex + 1) / 3) if lastSeenIndex != None else 0