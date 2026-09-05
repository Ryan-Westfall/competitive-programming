class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        MOD = 10**9 + 7
        BASE = 26

        seen = set()

        for word in dict:
            n = len(word)

            prefix = [0] * (n + 1)
            power = [1] * (n + 1)

            # Build prefix hashes and powers
            for i in range(n):
                val = ord(word[i]) - ord('a')

                prefix[i + 1] = (
                    prefix[i] * BASE + val
                ) % MOD

                power[i + 1] = (
                    power[i] * BASE
                ) % MOD

            for i in range(n):
                # hash before removed character
                left = prefix[i]

                # hash after removed character
                right = (
                    prefix[n]
                    - prefix[i + 1] * power[n - i - 1]
                ) % MOD

                # concatenate left + right
                deleted_hash = (
                    left * power[n - i - 1] + right
                ) % MOD

                key = (i, deleted_hash)

                if key in seen:
                    return True

                seen.add(key)

        return False