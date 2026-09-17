class Solution:
    def minHeightShelves(self, books: list[list[int]], shelfWidth: int) -> int:
        n = len(books)

        @cache
        def dp(i):
            if i == n:
                return 0

            curWidth = books[i][0]
            maxHeight = books[i][1]
            minHeight = dp(i+1) + maxHeight
            while i + 1 < n and curWidth + books[i+1][0] <= shelfWidth:
                i += 1
                curWidth += books[i][0]
                maxHeight = max(maxHeight, books[i][1])
                minHeight = min(minHeight, dp(i+1) + maxHeight)
            return minHeight


        return dp(0)