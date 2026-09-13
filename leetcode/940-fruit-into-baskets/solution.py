class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        holding = defaultdict(int)
        maxNum = 0
        l = 0

        for r in range(len(fruits)):
            holding[fruits[r]] += 1

            while len(holding.values()) > 2:
                holding[fruits[l]] -= 1
                if holding[fruits[l]] == 0:
                    del holding[fruits[l]]
                l += 1

            maxNum = max(maxNum, r - l + 1)

        return maxNum