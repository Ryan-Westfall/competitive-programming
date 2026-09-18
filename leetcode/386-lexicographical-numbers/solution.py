class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        ans = []

        def dfs(cur):
            if cur > n:
                return

            ans.append(cur)

            for digit in range(10):
                nxt = cur * 10 + digit

                if nxt > n:
                    break

                dfs(nxt)

        for i in range(1, 10):
            dfs(i)

        return ans