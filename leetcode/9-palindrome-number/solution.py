class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        c = x
        backwards = 0
        while c:
            backwards = backwards * 10 + c % 10
            c = c // 10
        return backwards == x