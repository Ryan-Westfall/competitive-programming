class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        pairs = sorted((num, i) for i, num in enumerate(nums))

        ans = nums[:]

        start = 0

        for end in range(1, len(pairs) + 1):
            if end == len(pairs) or pairs[end][0] - pairs[end - 1][0] > limit:
                group = pairs[start:end]

                values = [num for num, i in group]
                indices = sorted(i for num, i in group)

                for i, value in zip(indices, values):
                    ans[i] = value

                start = end

        return ans