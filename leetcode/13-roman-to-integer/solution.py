class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        output = 0;
        prev = "M"
        for i in range(len(s)):
            if ROMAN[prev] < ROMAN[s[i]]:
                output -= ROMAN[prev]
                output += ROMAN[s[i]] - ROMAN[prev]
                prev = s[i]
                print("yo")
                continue
            print("yo")
            output += ROMAN[s[i]]
            prev = s[i]
        return output