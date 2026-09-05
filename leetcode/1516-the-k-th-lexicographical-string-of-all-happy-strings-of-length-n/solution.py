class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        alphabet = {0:'a',1:'b',2:'c'}
        output = []
        def backtrack(cur):
            if len(cur) == n:
                output.append(cur[:])
                return

            if len(output) == k:
                return


            for i in range(0,3):
                char = alphabet[i]

                if cur and cur[-1] == char:
                    continue

                cur.append(char)
                backtrack(cur)
                cur.pop()

        backtrack([])
        # print(output)
        return "" if k > len(output) else "".join(output[k-1])