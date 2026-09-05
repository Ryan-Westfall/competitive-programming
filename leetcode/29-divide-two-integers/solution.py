class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 1. Handle overflow edge case up front
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        # 2. Determine the sign of the final result
        is_negative = (dividend < 0) ^ (divisor < 0)

        # 3. Work entirely with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)

        cur = 0
        res = 0

        # 4. Core binary long division loop
        for i in range(dividend.bit_length() - 1, -1, -1):
            bit = (dividend >> i) & 1
            cur = (cur << 1) | bit
            
            res = res << 1
            if cur >= divisor:
                cur -= divisor
                res |= 1

        # 5. Apply the sign mapping
        return -res if is_negative else res