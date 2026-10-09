
class Solution:
    def minInsertions(self, s: str) -> int:
        ans = 0
        need = 0  # Number of ')' characters still needed

        for c in s:
            if c == '(':
                # An odd number of ')' is needed: insert one to complete a pair
                if need % 2 == 1:
                    ans += 1
                    need -= 1

                # Every '(' requires two ')'
                need += 2

            else:  # c == ')'
                need -= 1

                # Too many ')' encountered; insert '(' to match this ')'
                if need < 0:
                    ans += 1
                    need = 1

        return ans + need
