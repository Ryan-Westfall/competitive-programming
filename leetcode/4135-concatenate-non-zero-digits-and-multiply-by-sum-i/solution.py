class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        sumX = 0
        place = 1  # Tracks 1s, 10s, 100s position
        
        while n:
            digit = n % 10
            
            if digit != 0:
                # Add the digit to the LEFT side of x
                x = x + (digit * place)
                sumX += digit
                # Only increase the place value when a non-zero digit is added
                place *= 10 
                
            n = n // 10
            
        return x * sumX
