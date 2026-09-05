class Solution:
    def minSwaps(self, data: List[int]) -> int:
        numberOfOnes = data.count(1)

        l = 0
        r = 0
        currentOnes = 0

        while (r-l) < numberOfOnes:
                if data[r] == 1:
                    currentOnes += 1
                r += 1

        if currentOnes == 0:
            return 0

        r -= 1

        maximumOnes = currentOnes

        while r < len(data):
            maximumOnes = max(maximumOnes, currentOnes)
            if data[l] == 1:
                currentOnes -= 1
            l += 1
            r += 1
            if r < len(data) and data[r] == 1:
                currentOnes += 1

        return numberOfOnes - maximumOnes
