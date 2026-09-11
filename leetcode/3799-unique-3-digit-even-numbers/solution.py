class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        cnt = [0] * 10

        for d in digits:
            cnt[d] += 1

        ans = 0

        for a in range(1, 10):       # hundreds: can't be 0
            if cnt[a] == 0:
                continue
            cnt[a] -= 1

            for b in range(10):     # tens
                if cnt[b] == 0:
                    continue
                cnt[b] -= 1

                for c in range(0, 10, 2):  # units: must be even
                    if cnt[c]:
                        ans += 1

                cnt[b] += 1

            cnt[a] += 1

        return ans