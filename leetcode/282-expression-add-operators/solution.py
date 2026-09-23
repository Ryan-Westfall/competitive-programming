class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        ans = []
        n = len(num)

        def dfs(i, value, prev, expr):
            if i == len(num):
                if value == target:
                    ans.append(expr)
                return

            for j in range(i, n):
                if j > i and num[i] == '0':
                    break

                cur = int(num[i:j + 1])

                if i == 0:
                    # First number: no operator
                    dfs(j + 1, cur, cur, str(cur))
                else:
                    # +
                    dfs(
                        j + 1,
                        value + cur,
                        cur,
                        expr + '+' + str(cur)
                    )

                    # -
                    dfs(
                        j + 1,
                        value - cur,
                        -cur,
                        expr + '-' + str(cur)
                    )

                    # *
                    dfs(
                        j + 1,
                        value - prev + prev * cur,
                        prev * cur,
                        expr + '*' + str(cur)
                    )

        dfs(0, 0, 0, "")
        return ans