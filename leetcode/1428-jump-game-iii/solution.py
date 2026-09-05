class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        @cache
        def canJump(i):
            if i >= n or i < 0 or i in visited:
                return False
            if arr[i] == 0:
                return True

            visited.add(i)

            return canJump(i + arr[i]) or canJump(i - arr[i])


        return canJump(start)