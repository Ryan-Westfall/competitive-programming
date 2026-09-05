import heapq
from typing import List

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Process courses in order of earliest deadline
        courses.sort(key=lambda x: x[1])

        max_heap = []  # Store negative durations to simulate a max heap
        total_time = 0

        for duration, last_day in courses:
            # Optimistically take the course
            total_time += duration
            heapq.heappush(max_heap, -duration)

            # If we've missed the current deadline,
            # remove the longest course we've taken so far
            if total_time > last_day:
                longest = -heapq.heappop(max_heap)
                total_time -= longest

        return len(max_heap)