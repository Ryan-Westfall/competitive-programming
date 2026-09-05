class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)

        if m > n:
            return 0

        BASE = 31
        MOD = 10**9 + 7

        # Hash of word
        target = 0
        for c in word:
            target = (target * BASE + (ord(c) - ord('a') + 1)) % MOD

        # Prefix hashes and powers
        prefix = [0] * (n + 1)
        power = [1] * (n + 1)

        for i in range(n):
            power[i + 1] = (power[i] * BASE) % MOD
            prefix[i + 1] = (
                prefix[i] * BASE + (ord(sequence[i]) - ord('a') + 1)
            ) % MOD

        def getHash(l, r):
            # inclusive
            return (
                prefix[r + 1]
                - prefix[l] * power[r - l + 1]
            ) % MOD

        dp = [0] * n
        ans = 0

        for end in range(m - 1, n):
            start = end - m + 1

            if getHash(start, end) == target:
                # Collision check (optional for interviews, recommended in production)
                if sequence[start:end + 1] == word:
                    dp[end] = 1
                    if end >= 2 * m - 1:
                        dp[end] += dp[end - m]
                    ans = max(ans, dp[end])

        return ans