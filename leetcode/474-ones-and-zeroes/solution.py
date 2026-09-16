class Solution:
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        nLen = len(strs)
        counter = defaultdict(list)


        for i, item in enumerate(strs):
            counter[i].append(item.count('0'))
            counter[i].append(item.count('1'))


        @cache
        def dp(i, curM, curN):
            if curM < 0 or curN < 0:
                return -1

            if i == nLen:
                return 0

            curZero, curOne = counter[i]
            take = dp(i+1, curM - curZero, curN - curOne) + 1

            noTake = dp(i+1, curM, curN)
            return max(take, noTake)


            

        return dp(0, m, n)