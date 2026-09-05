class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary = ""

        for c in s:
            binary += format(ord(c), "08b")

        return binary == binary[::-1]