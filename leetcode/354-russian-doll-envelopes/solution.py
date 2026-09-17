class Solution:
    def maxEnvelopes(self, envelopes: list[list[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        n = len(envelopes)
        tails = []

        for curWidth, curHeight in envelopes:
            i = bisect_left(tails, curHeight)
            if i == len(tails):
                tails.append(curHeight)
            else:
                tails[i] = curHeight
        
        return len(tails)