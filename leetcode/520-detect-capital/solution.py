class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lowercase_detected = False
        first_uppercase_detected = False
        uppercase_detected = False

        for i, s in enumerate(word):
            if i == 0 and s < 'a':
                first_uppercase_detected = True
            elif s < 'a':
                uppercase_detected = True
            else:
                lowercase_detected = True

            if uppercase_detected and lowercase_detected:
                return False

        return True