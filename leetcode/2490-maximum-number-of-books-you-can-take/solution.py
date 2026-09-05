class Solution:
    def maximumBooks(self, books: List[int]) -> int:
        n = len(books)

        left = [-1] * n
        stack = []

        # Find previous j where:
        # books[j] - j < books[i] - i
        for i in range(n):
            while stack and books[stack[-1]] - stack[-1] >= books[i] - i:
                stack.pop()

            if stack:
                left[i] = stack[-1]

            stack.append(i)

        @cache
        def takeMost(i):
            if i < 0:
                return 0

            j = left[i]

            # We want the sequence ending at books[i]:
            #
            # ..., books[i]-2, books[i]-1, books[i]
            #
            # There are at most i-j shelves available,
            # but we also can't go below 1.
            count = min(books[i], i - j)

            smallest = books[i] - count + 1

            # arithmetic sequence:
            # smallest + ... + books[i]
            total = (smallest + books[i]) * count // 2

            if j != -1:
                total += takeMost(j)

            return total

        return max(takeMost(i) for i in range(n))