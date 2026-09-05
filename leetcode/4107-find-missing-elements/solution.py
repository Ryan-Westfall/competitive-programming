class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        least = float('inf')
        most = float('-inf')
        seen = set()
        for num in nums:
            least = min(least, num)
            most = max(most, num)
            seen.add(num)


        output = []
        if len(seen) == most - least + 1:
            return output

        for i in range(least + 1, most):
            if i not in seen:
                output.append(i)

        return output
