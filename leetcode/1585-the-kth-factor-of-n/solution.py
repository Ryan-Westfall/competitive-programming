class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        small = deque()
        large = deque()

        for i in range(1,int(sqrt(n))+1):
            if n % i == 0:
                small.append(i)
                if i != n//i:
                    large.appendleft(n//i)

        small.extend(large)
        if k > len(small):
            return -1

        return small[k-1]
