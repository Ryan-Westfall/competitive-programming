class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(cur,firstNum):
            if len(cur) == k:
                output.append(cur[:])
                return

            need = k - len(cur)
            remain = n - firstNum + 1
            available = remain - need

            for num in range(firstNum, firstNum + available + 1):
                cur.append(num)
                backtrack(cur, num + 1)
                cur.pop()

        backtrack([],1)

        return output