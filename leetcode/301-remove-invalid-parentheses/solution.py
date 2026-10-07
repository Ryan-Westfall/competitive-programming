class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left_remove = 0
        right_remove = 0

        for c in s:
            if c == '(':
                left_remove += 1
            elif c == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        output = set()

        def backtracking(i, cur, openP, left_remove, right_remove):
            if i == len(s):
                if openP == 0 and left_remove == 0 and right_remove == 0:
                    output.add("".join(cur))
                return

            c = s[i]

            # NoTake
            if c == '(' and left_remove > 0:
                backtracking(i + 1, cur, openP, left_remove - 1, right_remove)

            elif c == ')' and right_remove > 0:
                backtracking(i + 1, cur, openP, left_remove, right_remove - 1)

            # Take
            if c == '(':
                backtracking(i + 1, cur + [c], openP + 1,
                             left_remove, right_remove)

            elif c == ')':
                if openP > 0:
                    backtracking(i + 1, cur + [c], openP - 1,
                                 left_remove, right_remove)

            else:
                backtracking(i + 1, cur + [c], openP,
                             left_remove, right_remove)

        backtracking(0, [], 0, left_remove, right_remove)

        return list(output)