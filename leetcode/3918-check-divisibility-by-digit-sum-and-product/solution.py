class Solution:
    def checkDivisibility(self, n: int) -> bool:
        
        num = n
        aSum = 0
        pSum = 1
        while num > 0:
            digit = num % 10
            aSum += digit
            pSum *= digit
            num //= 10

        if n % (aSum + pSum) == 0:
            return True
        else:
            return False
        

        
        