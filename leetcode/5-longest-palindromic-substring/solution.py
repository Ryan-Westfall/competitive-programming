class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxSubstring = ""
        
        for i in range(len(s)):
            l = r = i
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                temp = s[l:r+1]
                if len(temp) > len(maxSubstring):
                    maxSubstring = temp
                l -= 1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                temp = s[l:r+1]
                if len(temp) > len(maxSubstring):
                    maxSubstring = temp
                l -= 1
                r += 1
                
                
        return maxSubstring