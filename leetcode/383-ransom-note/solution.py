class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter = Counter(magazine)

        for c in ransomNote:
            if counter[c]:
                counter[c] -= 1
            else:
                return False

        return True