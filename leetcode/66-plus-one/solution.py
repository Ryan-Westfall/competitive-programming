class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        count = 0
        while digits and digits[-1] + 1 == 10:
            digits.pop()
            count += 1

        if digits:
            digits[-1] += 1
        else:
            digits = [1]

        digits = digits + [0] * count
        return digits

        