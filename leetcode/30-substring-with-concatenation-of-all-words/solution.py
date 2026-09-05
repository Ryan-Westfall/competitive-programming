from collections import Counter
from typing import List

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)  # Target frequency map
        output = []
        
        # We run the sliding window word_len times to catch all offset positions
        for i in range(word_len):
            l = i
            r = i
            current_counts = Counter()
            words_matched = 0
            
            # Slide the window across the string by word_len increments
            while r + word_len <= len(s):
                # Grab the next word chunk
                word = s[r:r + word_len]
                r += word_len
                
                # Case 1: The word is part of our target list
                if word in word_counts:
                    current_counts[word] += 1
                    words_matched += 1
                    
                    # If we have too many copies of this word, shrink left until valid
                    while current_counts[word] > word_counts[word]:
                        left_word = s[l:l + word_len]
                        current_counts[left_word] -= 1
                        words_matched -= 1
                        l += word_len
                    
                    # If total word count matches, we found a complete permutation
                    if words_matched == num_words:
                        output.append(l)
                        
                # Case 2: The word is completely invalid, reset the window
                else:
                    current_counts.clear()
                    words_matched = 0
                    l = r
                    
        return output