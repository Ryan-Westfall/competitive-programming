class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1

        queue = deque()
        if n % 2 == 1:
            queue.append(s[n // 2])
        for i in range(len(count) - 1, -1, -1):
            if count[i] >= 2:
                c = chr(97 + i) * (count[i] // 2)
                queue.append(c)
                queue.appendleft(c)

        return "".join(queue)
        
