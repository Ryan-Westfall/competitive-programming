from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        memo = {}  # Memoization dictionary

        def backtrack(row, col, prev):
            # Base case: Out of bounds or not strictly increasing
            if row < 0 or row >= ROW or col < 0 or col >= COL or matrix[row][col] <= prev:
                return 0
            
            # If the result for the current cell is already computed, return it
            if (row, col) in memo:
                return memo[(row, col)]
            
            # Explore all four possible directions
            max_length = 0
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                max_length = max(max_length, backtrack(row + dr, col + dc, matrix[row][col]))
            
            # Add 1 for the current cell and store the result in memo
            memo[(row, col)] = 1 + max_length
            return memo[(row, col)]

        max_length = 0
        # Start backtracking from every cell in the matrix
        for r in range(ROW):
            for c in range(COL):
                max_length = max(max_length, backtrack(r, c, -1))

        return max_length
