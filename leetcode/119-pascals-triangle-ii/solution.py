class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ans = []

        for i in range(rowIndex + 1):
            ans.append(1)
            prev = ans.copy()
            for j in range(1, i):
                ans[j] = prev[j-1] + prev[j]

        return ans
