class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        previous = self.countAndSay(n - 1)

        result = []
        i = 0

        while i < len(previous):
            count = 1

            while i + 1 < len(previous) and previous[i] == previous[i + 1]:
                count += 1
                i += 1

            result.append(str(count))
            result.append(previous[i])
            i += 1

        return "".join(result)