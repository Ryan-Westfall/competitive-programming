from typing import List
import math

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        minimum = float('inf')
        for i, freq in enumerate(count):
            if freq:
                minimum = i
                break

        # FIX 1: maximum
        for i in range(255, -1, -1):
            if count[i]:
                maximum = i
                break

        totalSum = 0
        totalNum = 0
        for num, freq in enumerate(count):
            totalSum += num * freq
            totalNum += freq

        mean = totalSum / totalNum

        mode = 0
        modeNum = 0
        for num, freq in enumerate(count):
            if freq > mode:
                mode = freq
                modeNum = num

        # FIX 2: odd/even cases were backwards
        if totalNum % 2 == 1:
            target = totalNum // 2 + 1
            runningCount = 0

            for i, freq in enumerate(count):
                runningCount += freq
                if runningCount >= target:
                    median = float(i)
                    break
        else:
            leftTarget = totalNum // 2
            rightTarget = leftTarget + 1

            runningCount = 0
            left = right = None

            for i, freq in enumerate(count):
                runningCount += freq

                # FIX 3: variable names
                if left is None and runningCount >= leftTarget:
                    left = i

                if runningCount >= rightTarget:
                    right = i
                    break

            median = (left + right) / 2

        # FIX 4: compute stddev
        # variance = 0
        # for value, freq in enumerate(count):
        #     variance += freq * ((value - mean) ** 2)

        # variance /= totalNum
        # stddev = math.sqrt(variance)

        return [
            float(minimum),
            float(maximum),
            mean,
            median,
            float(modeNum)
        ]