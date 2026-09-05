class Solution:
    def beautifulSplits(self, nums: List[int]) -> int:
        n = len(nums)

        MOD = 1_000_000_007
        BASE = 911382323

        prefix = [0] * (n + 1)
        power = [1] * (n + 1)

        for i, x in enumerate(nums):
            prefix[i + 1] = (prefix[i] * BASE + x) % MOD
            power[i + 1] = (power[i] * BASE) % MOD

        def get_hash(l, r):
            return (
                prefix[r] -
                prefix[l] * power[r - l]
            ) % MOD

        count = 0

        for i in range(1, n - 1):
            for j in range(i + 1, n):
                len1 = i
                len2 = j - i
                len3 = n - j

                first = (
                    len1 <= len2
                    and get_hash(0, i) == get_hash(i, i + i)
                )

                second = (
                    len2 <= len3
                    and get_hash(i, j) == get_hash(j, j + len2)
                )

                if first or second:
                    count += 1

        return count