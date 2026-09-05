class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        smallestTime = events[0][1]
        smallestButton = events[0][0]
        delta = 0
        for i in range(len(events) - 1):
            button, time = events[i]
            nextButton, nextTime = events[i+1]

            delta = nextTime - time
            if delta >= smallestTime:
                if delta == smallestTime:
                    smallestButton = min(nextButton, smallestButton)
                else:
                    smallestButton = nextButton
                smallestTime = delta


        return smallestButton

            
        