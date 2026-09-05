class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixSum = [0] * (len(gain) + 1)

        for i, elv in enumerate(gain):
            prefixSum[i + 1] = prefixSum[i] + elv


        return max(prefixSum)