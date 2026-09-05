class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        curIndex = 0
        for num in range(1, n + 1):
            stack.append("Push")
            if target[curIndex] != num:
                stack.append("Pop")
            else:
                curIndex += 1

            # print(num, curIndex, target[curIndex])

            if curIndex > len(target) - 1:
                return stack

        return stack