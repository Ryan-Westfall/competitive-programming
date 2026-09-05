class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] #stack of indexes

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                lastIndex = stack.pop()
                output[lastIndex] = i - lastIndex
            stack.append(i)

        return output