class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)  # Difference array

        # Apply the queries to the difference array
        for l, r in queries:
            diff[l] -= 1
            if r + 1 < n:
                diff[r + 1] += 1

        # Compute the actual nums array after all queries
        current = 0
        for i in range(n):
            current += diff[i]
            nums[i] += current


        # Check if all elements are 0
        return all(x <= 0 for x in nums)
