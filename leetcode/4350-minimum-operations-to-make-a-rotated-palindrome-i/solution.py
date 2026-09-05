class Solution:
    
    def minOperations(self, s: str) -> int:
        output = float('inf')

        
        for k in range(len(s)):
            cost = k
            left = 0
            right = len(s) - 1

            while left < right:
                a = s[(k+left) % (len(s))]
                b = s[(k+right) % (len(s))]
                delta = abs(ord(a) - ord(b))
                cost += min(delta, 26 - delta)

                left += 1
                right -= 1

            output = min(output, cost)

        return output
            
            
                
        




        
       

        