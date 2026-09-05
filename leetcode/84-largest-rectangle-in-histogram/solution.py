class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxSeen = 0
        stack = [] # (value, index)
        for i in range(len(heights)):
            lastIndex = i
            while stack and heights[i] <= stack[-1][0]:
                lastValue, lastIndex = stack.pop()
                maxSeen = max(maxSeen, lastValue * (i - lastIndex))
            stack.append((heights[i], lastIndex))

        # Process after stack built
        length = len(heights)
        while stack:
            value, index = stack.pop()
            maxSeen = max(maxSeen, (length - index) * value)

        return maxSeen