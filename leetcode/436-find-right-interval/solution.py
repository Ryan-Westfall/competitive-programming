class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        arr = sorted([(s, e, i) for i, (s, e) in enumerate(intervals)])

        output = [-1] * len(intervals)

        for idx, (s, e) in enumerate(intervals):
            l, r = 0, len(arr) - 1
            ans = -1

            while l <= r:
                mid = (l + r) // 2

                if arr[mid][0] >= e:
                    ans = arr[mid][2]
                    r = mid - 1
                else:
                    l = mid + 1

            output[idx] = ans

        return output