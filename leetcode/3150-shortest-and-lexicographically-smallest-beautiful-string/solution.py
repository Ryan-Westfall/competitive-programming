class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        count = 0
        best = ""

        for right in range(len(s)):
            if s[right] == '1':
                count += 1

            while count > k:
                if s[left] == '1':
                    count -= 1
                left += 1

            while count == k:
                candidate = s[left:right + 1]

                if not best or len(candidate) < len(best) or (len(candidate) == len(best) and candidate < best):
                    best = candidate

                if s[left] == '1':
                    count -= 1
                left += 1

        return best