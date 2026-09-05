class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        dictionary = defaultdict(set)

        for row, seat in reservedSeats:
            dictionary[row].add(seat)

        count = (n - len(dictionary)) * 2

        for reserved in dictionary.values():
            left = reserved.isdisjoint({2, 3, 4, 5})
            right = reserved.isdisjoint({6, 7, 8, 9})
            middle = reserved.isdisjoint({4, 5, 6, 7})

            if left and right:
                count += 2
            elif left or right or middle:
                count += 1

        return count