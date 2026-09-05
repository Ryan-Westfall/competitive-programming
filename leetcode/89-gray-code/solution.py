class Solution:
    def grayCode(self, n: int) -> List[int]:
        output = [0]

        def permutation(bit):
            if bit == n:
                return

            for i in range(len(output) - 1, -1, -1):
                output.append(output[i] | (1 << bit))

            permutation(bit + 1)

        permutation(0)

        return output