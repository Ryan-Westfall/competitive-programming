class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = [interval[0] for interval in intervals]
        end = [interval[1] for interval in intervals]
        start.sort()
        end.sort()

        s = 0
        e = 0

        count = 0
        maxCount = 0

        while s <= len(start) - 1:
            if start[s] < end[e]:
                s += 1
                count += 1
                maxCount = max(count, maxCount)
            elif start[s] == end[e]:
                s += 1
                e += 1
            else:
                e += 1
                count -= 1

        return maxCount
            
