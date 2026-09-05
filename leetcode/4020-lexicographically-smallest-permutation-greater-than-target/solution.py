class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = Counter(s)
        n = len(s)

        # Build the prefix that is equal to target as long as possible.
        ans = []

        for i in range(n):
            if count[target[i]] > 0:
                ans.append(target[i])
                count[target[i]] -= 1
            else:
                break
        else:
            # We matched target completely.
            # Need to increase some earlier character.
            i = n - 1

        # Try to make the answer greater.
        # First try at the position where matching failed.
        while i >= 0:
            if i < len(ans):
                # Put back the character we previously used.
                count[ans[i]] += 1
                ans.pop()

            # Find the smallest character > target[i].
            for c in sorted(count):
                if c > target[i] and count[c] > 0:
                    count[c] -= 1

                    result = ans + [c]

                    # Fill remaining positions with smallest characters.
                    for x in sorted(count):
                        result.extend([x] * count[x])

                    return "".join(result)

            i -= 1

        return ""