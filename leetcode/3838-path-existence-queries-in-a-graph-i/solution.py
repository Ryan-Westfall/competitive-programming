class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        groupMap = defaultdict(set)

        for i in range(1, len(nums)):
            difference = abs(nums[i-1] - nums[i])
            if difference <= maxDiff:
                persistSet = groupMap[i-1]
                persistSet.add(i-1)
                persistSet.add(i)
                groupMap[i] = persistSet

        output = [False] * len(queries)
        for i, query in enumerate(queries):
            source, destination = query
            output[i] = (source in groupMap[destination] and destination in groupMap[source]) or source == destination

        return output

