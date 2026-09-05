class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for word in wordSet:
                end = i + len(word)

                if end <= len(s) and s[i:end] == word:
                    if dfs(end):
                        memo[i] = True
                        return True

            memo[i] = False
            return False

        return dfs(0)