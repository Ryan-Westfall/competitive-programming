class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        counter = {}

        for t in time:
            counter[t % 60] = 1 + counter.get(t % 60, 0)


        pairs = 0
        for k, v in counter.items():

            if k < 30 and 60 - k in counter:
                matches = counter[60 -k]
                pairs += v * matches

            # print(k, pairs)

            if k == 30 or k == 0:
                if v >= 2:
                    while v:
                        pairs += (v - 1)
                        v -= 1

            # print(k, pairs)

        return pairs


        