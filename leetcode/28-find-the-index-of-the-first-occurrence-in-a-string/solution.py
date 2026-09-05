class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) + 1 - len(needle)):
            checkIndex = 0
            while haystack[i + checkIndex] == needle[checkIndex]:
                checkIndex += 1
                if checkIndex == len(needle):
                    return i

        return -1