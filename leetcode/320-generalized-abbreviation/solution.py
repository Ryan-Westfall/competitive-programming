class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        res = []

        def dfs(index: int, count: int, path: List[str]) -> None:
            # Reached the end of the word
            if index == len(word):
                if count:
                    path.append(str(count))
                res.append("".join(path))
                if count:
                    path.pop()
                return

            # Choice 1: Abbreviate this character
            dfs(index + 1, count + 1, path)

            # Choice 2: Keep this character
            if count:
                path.append(str(count))
            path.append(word[index])

            dfs(index + 1, 0, path)

            # Backtrack
            path.pop()          # Remove character
            if count:
                path.pop()      # Remove count

        dfs(0, 0, [])
        return res