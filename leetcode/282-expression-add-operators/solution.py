class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        def dfs(index, curArr, curSum, prev):
            if index == len(num):
                if curSum == target:
                    result.append("".join(curArr))
                return
            else:
                for i in range(index, len(num)):
                    curStr = num[index: i + 1]
                    curNum = int(curStr)

                    if not curArr:
                        dfs(i + 1, [curStr], curNum, curNum)
                    else:
                        dfs(i + 1, curArr + ['+'] + [curStr], curSum + curNum, curNum)
                        dfs(i + 1, curArr + ['-'] + [curStr], curSum - curNum, -curNum)
                        dfs(i + 1, curArr + ['*'] + [curStr], (curSum - prev) + (curNum * prev), curNum * prev)


                    if num[index] == '0':
                        break


        dfs(0, [], 0, 0)
        return result

        # Time Complexity: O(4^n) * n
        # Space Complexity: O(n)