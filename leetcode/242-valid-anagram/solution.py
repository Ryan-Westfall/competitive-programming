class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        seen2 = {}
        for i in s:
            seen1[i] = seen1.get(i, 0) + 1
        
        for i in t:
            seen2[i] = seen2.get(i, 0) + 1

        return seen1 == seen2