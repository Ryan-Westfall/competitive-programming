class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        sortedI = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        n = len(startTime)

        @cache
        def mostMoney(i):
            if i == n:
                return 0

            # bs for first compatible endTime
            l = i
            r = n
            while l < r:
                mid = l + (r - l) // 2
                if sortedI[i][1] <= sortedI[mid][0]:
                    r = mid
                else:
                    l = mid + 1

            # Take and do next compatible, OR don't take and go next
            return max(sortedI[i][2] + mostMoney(l), mostMoney(i+1))
            
        return mostMoney(0)

        
