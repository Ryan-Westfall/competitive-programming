class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()

        output = 0
        l = 0
        r = len(tokens) - 1
        while l < len(tokens) and tokens[l] <= power:
            power -= tokens[l]
            l += 1
            output += 1
            if l < len(tokens) and l != r and tokens[l] > power and tokens[r] + power >= tokens[l]:
                power += tokens[r]
                r -= 1
                output -= 1

        return output
            