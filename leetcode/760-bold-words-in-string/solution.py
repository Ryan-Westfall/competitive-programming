class Solution:
    def boldWords(self, words: List[str], s: str) -> str:
        lengths = set(len(word) for word in words)
        hashes = set()

        base = 31
        mod = 10 ** 9 + 7
        for word in words:
            curHash = 0
            for i, c in enumerate(word):
                curHash = ((base * curHash) + (ord(c) - ord('a') + 1)) % mod
            hashes.add(curHash)

        n = len(s)
        prefix = [0] * (n + 1)
        power = [1] * (n + 1)
        for i, c in enumerate(s):
            prefix[i + 1] = (prefix[i] * base + (ord(c) - ord('a') + 1)) % mod
            power[i + 1] = (power[i] * base) % mod

        def getHash(l, r):
            return (prefix[r] - prefix[l] * power[r-l]) % mod

        # l & r
        stack = []
        for i in range(n - min(lengths) + 1):
            for length in lengths:
                if i + (length - 1) >= n:
                    continue
                if getHash(i, i + (length )) in hashes:
                    if stack and i <= stack[-1][1] + 1:
                        stack[-1][1] = max(stack[-1][1], i + length - 1)
                    else:
                        stack.append([i, i + length - 1])

        while stack:
            left, right = stack.pop()
            s = s[:left] + "<b>" + s[left:right + 1] + "</b>" + s[right + 1:]

        return s


        
        