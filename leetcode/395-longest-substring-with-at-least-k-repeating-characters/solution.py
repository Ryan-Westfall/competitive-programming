from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # Call the helper function with the initial range covering the entire string
        return self.longestSubstringUtil(s, 0, len(s), k)

    def longestSubstringUtil(self, s: str, start: int, end: int, k: int) -> int:
        # If the length of the current substring is less than k, return 0
        # because no valid substring can exist
        if end - start < k:
            return 0
        
        # Use Counter to count the frequency of each character in the substring
        count_map = Counter(s[start:end])
        
        # Iterate over each character in the current range
        for mid in range(start, end):
            # If the character's frequency is >= k, continue to the next character
            if count_map[s[mid]] >= k:
                continue
            
            # Recursively process the left and right parts divided by the current "mid" point
            return max(
                # Recursively process the left part of the substring (start to mid)
                self.longestSubstringUtil(s, start, mid, k),
                # Recursively process the right part of the substring (mid + 1 to end)
                self.longestSubstringUtil(s, mid + 1, end, k)
            )
        
        # If all characters in the substring meet the condition, return its length
        return end - start
