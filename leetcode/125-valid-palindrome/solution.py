class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            # Move left pointer to the next alphanumeric character
            while l < r and not s[l].isalnum():
                l += 1
            # Move right pointer to the next alphanumeric character
            while l < r and not s[r].isalnum():
                r -= 1

            # Compare characters in a case-insensitive manner
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


