class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        curDigit = 0
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                while j < len(abbr) and abbr[j].isdigit():
                    curDigit = curDigit * 10 + int(abbr[j])
                    if curDigit == 0:
                        return False
                    j += 1
                i += curDigit
                curDigit = 0
                continue
            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1


        return len(word) == i and len(abbr) == j
