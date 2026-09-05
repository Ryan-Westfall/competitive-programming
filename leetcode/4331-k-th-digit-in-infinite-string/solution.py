class Solution:
    def kthDigit(self, k: int) -> int:
        if k <= 9:
            return k

        digitsSeen = 9
        b = 1

        while True:
            d = len(str(b * 10))

            # Number of blocks with d-digit numbers
            blocks = 9 * 10 ** (d - 2)

            digitsInBlocks = blocks * 10 * d

            if digitsSeen + digitsInBlocks >= k:
                break

            digitsSeen += digitsInBlocks
            b += blocks

        # Find the exact block
        blockPosition = k - digitsSeen - 1

        b += blockPosition // (10 * d)
        blockPosition %= 10 * d

        numberIndex = blockPosition // d
        digitIndex = blockPosition % d

        if b % 2 == 0:
            number = 10 * b + numberIndex
        else:
            number = 10 * b + (9 - numberIndex)

        return int(str(number)[digitIndex])