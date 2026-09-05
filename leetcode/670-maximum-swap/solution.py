class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        maxSeenIndex = len(num) - 1
        maxSeen = "-1"
        maxInfo = [None] * len(num)  # Store (maxSeen, maxSeenIndex) for each position

        for i in range(len(num) - 1, -1, -1):
            maxInfo[i] = (maxSeen, maxSeenIndex)  # Store current max
            if num[i] > maxSeen:
                maxSeen = num[i]
                maxSeenIndex = i


        for i in range(len(num)):
            maxSeen, maxSeenIndex = maxInfo[i]

            if maxSeen > num[i]:
                num[i], num[maxSeenIndex] = num[maxSeenIndex], num[i]
                break

        return int("".join(num))  # Convert back to int
        