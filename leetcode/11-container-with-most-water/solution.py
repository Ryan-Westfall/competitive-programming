class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        output = 0
        while left < right:
            lHeight = height[left]
            rHeight = height[right]
            output = max(output, min(lHeight, rHeight) * (right - left))

            if lHeight >= rHeight:
                right -= 1
            else:
                left += 1

        return output
