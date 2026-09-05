class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openCount = 0
        invalid = 0
        for c in s:
            if c == '(':
                openCount += 1
            elif openCount and c == ')':
                openCount -= 1
            else:
                invalid += 1

        return invalid + openCount