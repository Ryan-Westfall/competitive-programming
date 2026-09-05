class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        length = (1 << n) - 1
        inverse = False

        while k > 1:

            if k == length // 2 + 1:
                return "1" if not inverse else "0"

            if k > length // 2:
                k = length + 1 -k
                inverse = not inverse
            
            
            length //= 2
                
        return "0" if not inverse else "1"