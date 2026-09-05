class Solution:
    def countTasks(self, tasks: List[int], shifts: List[int]) -> List[int]:
        prefix = [0]
        for t in tasks:
            prefix.append(prefix[-1] + t)

        total = prefix[-1]
        progress = 0
        ans = []

        for shift in shifts:
            progress += shift

            if progress >= total:
                ans.append(0)
                progress = 0

            else:
                curT = bisect_right(prefix, progress) - 1
                ans.append(len(tasks) - curT)

        return ans
            