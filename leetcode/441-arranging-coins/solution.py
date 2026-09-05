class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        '''
        bruteforce way
        current = 0
        increment = 1
        count = 0
        while current < n:
            count += 1
            current += increment
            if current > n:
                return count - 1
            elif current == n:
                return count
            increment += 1
        '''
        #binary search
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right