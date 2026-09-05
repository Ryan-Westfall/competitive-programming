class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []

        def dfs(sumC, curArr, i):
            if sumC == target:
                output.append(curArr.copy())
                return
            if sumC > target or i >= len(candidates):
                print(curArr)
                return

            dfs(sumC, curArr, i+1)
            curArr.append(candidates[i])
            dfs(sumC + candidates[i], curArr, i)
            curArr.pop()
        
        dfs(0, [], 0)
        return output