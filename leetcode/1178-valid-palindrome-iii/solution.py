class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        self.string = s

        if not k:
            return self.isPalindrome(0, len(s) - 1)

        memo = {} #(l,r,k) = Boolean

        def dfs(l,r,k):
            if (l,r,k) in memo:
                return memo[(l,r,k)]
            elif not k:
                memo[(l,r,k)] = self.isPalindrome(l,r)
            else:
                while l < r:
                    if self.string[l] != self.string[r]:
                        memo[(l,r,k)] = dfs(l+1, r, k-1) or dfs(l,r-1,k-1)
                        return memo[(l,r,k)]

                    l += 1
                    r -= 1
                memo[(l,r,k)] = True
            return memo[(l,r,k)]
        
        return dfs(0, len(self.string) - 1, k)
            
    
    def isPalindrome(self, l, r) -> bool:
        while l < r:
            if self.string[l] != self.string[r]:
                return False
            l += 1
            r -= 1
        return True