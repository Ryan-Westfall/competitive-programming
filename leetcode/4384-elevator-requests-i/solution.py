class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        stack = [0]
        totalTime = 0
        for request in requests:
            delta = abs(stack[-1] - request)
            totalTime += delta
            stack.append(request)

        return totalTime