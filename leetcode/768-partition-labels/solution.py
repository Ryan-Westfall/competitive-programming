class Solution(object):
    def partitionLabels(self, S):
        ans = []
        lastValues = {item: count for count, item in enumerate(S)}
        left = right = 0;
        for count, item in enumerate(S):
            if lastValues[item] > right:
                right = lastValues[item]
            if count == right:
                ans.append(right - left + 1)
                left = count + 1
        return ans