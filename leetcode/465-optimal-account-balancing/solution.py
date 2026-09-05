class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        from collections import defaultdict

        balance = defaultdict(int)

        # Compute each person's net balance
        for frm, to, amount in transactions:
            balance[frm] -= amount
            balance[to] += amount

        # Keep only non-zero balances
        debt = [x for x in balance.values() if x != 0]

        def dfs(start: int) -> int:
            # Skip people already settled
            while start < len(debt) and debt[start] == 0:
                start += 1

            if start == len(debt):
                return 0

            ans = float("inf")

            for j in range(start + 1, len(debt)):
                # Must have opposite signs
                if debt[start] * debt[j] < 0:
                    # Settle start with j
                    debt[j] += debt[start]

                    ans = min(ans, 1 + dfs(start + 1))

                    # Backtrack
                    debt[j] -= debt[start]

                    # Pruning:
                    # If they perfectly cancel, no need to try other partners.
                    if debt[j] + debt[start] == 0:
                        break

            return ans

        return dfs(0)