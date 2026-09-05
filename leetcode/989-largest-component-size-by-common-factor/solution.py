class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        largest = max(nums)

        parent = [i for i in range(len(nums))]
        rank = [0] * len(nums)

        spf = [i for i in range(largest + 1)]

        for p in range(2, largest + 1):
            if spf[p] == p:
                for multiple in range(p * p, largest + 1, p):
                    if spf[multiple] == multiple:
                        spf[multiple] = p

        primeOwner = {}

        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px = find(x)
            py = find(y)

            if px == py:
                return

            if rank[px] < rank[py]:
                px, py = py, px

            parent[py] = px

            if rank[px] == rank[py]:
                rank[px] += 1

        for i, num in enumerate(nums):
            while num > 1:
                factor = spf[num]

                if factor in primeOwner:
                    union(primeOwner[factor], i)
                else:
                    primeOwner[factor] = i

                while num % factor == 0:
                    num //= factor

        counts = [0] * len(nums)
        for i in range(len(nums)):
            root = find(i)
            counts[root] += 1

        return max(counts)