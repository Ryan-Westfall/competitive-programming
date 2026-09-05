class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 1
        seen = set(s[l])
        maxSeen = len(seen)
        while r <= len(s) - 1:
            right = s[r]
            if right not in seen:
                seen.add(s[r])
                maxSeen = max(maxSeen, r - l + 1)
            else:
                while right in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
            r += 1
        return maxSeen
