class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = [0] * 26

        for c in p:
            target[ord(c) - ord('a')] += 1

        cur = [0] * 26

        need = 0
        for count in target:
            if count > 0:
                need += 1

        matches = 0
        l = 0
        output = []

        for r in range(len(s)):
            i = ord(s[r]) - ord('a')

            # Adding this character
            if target[i] > 0:
                if cur[i] == target[i]:
                    matches -= 1

                cur[i] += 1

                if cur[i] == target[i]:
                    matches += 1
            else:
                cur[i] += 1

            # Window too large
            while r - l + 1 > len(p):
                i = ord(s[l]) - ord('a')

                if target[i] > 0:
                    if cur[i] == target[i]:
                        matches -= 1

                    cur[i] -= 1

                    if cur[i] == target[i]:
                        matches += 1
                else:
                    cur[i] -= 1

                l += 1

            if matches == need:
                output.append(l)

        return output