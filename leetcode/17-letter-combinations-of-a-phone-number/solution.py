class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        mappings = {2: ['a','b','c'], 3: ['d','e','f'], 4: ['g','h','i'], 5:['j','k','l'], 
        6: ['m','n','o'], 7: ['p','q','r','s'], 8: ['t','u','v'], 9: ['w','x','y','z']}
        
        results = []
        subsets = []
        def dfs(index):
            if index >= len(digits):
                results.append(''.join(subsets))
                return

            for c in mappings[int(digits[index])]:
                subsets.append(c)
                dfs(index + 1)
                subsets.pop()

        dfs(0)
        return results