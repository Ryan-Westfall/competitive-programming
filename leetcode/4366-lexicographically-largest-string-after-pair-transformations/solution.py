class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        output = []

        for num in nums:
            cur = deque([])

            for bit in range(25):
                if num & 1:
                    cur.appendleft(chr(ord('a') + bit))
                num >>= 1

            cur.extendleft('z' * num)

            output.append("".join(cur))

        return output