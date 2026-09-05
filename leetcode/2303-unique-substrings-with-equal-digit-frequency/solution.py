class Solution:
    def equalDigitFrequency(self, s: str) -> int:
        MOD = 10**9 + 7
        BASE = 11

        n = len(s)

        # prefix hashes
        prefix = [0] * (n + 1)
        power = [1] * (n + 1)

        for i in range(n):
            prefix[i + 1] = (prefix[i] * BASE + int(s[i]) + 1) % MOD
            power[i + 1] = (power[i] * BASE) % MOD

        seen = set()

        for i in range(n):
            freq = [0] * 10
            distinct = 0
            maxFreq = 0

            for j in range(i, n):
                d = int(s[j])

                freq[d] += 1

                if freq[d] == 1:
                    distinct += 1

                maxFreq = max(maxFreq, freq[d])

                length = j - i + 1

                if maxFreq * distinct == length:
                    # Hash of s[i:j+1]
                    h = (
                        prefix[j + 1]
                        - prefix[i] * power[length]
                    ) % MOD

                    seen.add(h)

        return len(seen)