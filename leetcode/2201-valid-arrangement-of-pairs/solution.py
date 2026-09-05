class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adjList = defaultdict(list)
        inDegree = defaultdict(int)
        outDegree = defaultdict(int)
        for src, dst in pairs:
            adjList[src].append(dst)
            inDegree[dst] += 1
            outDegree[src] += 1


        start = None
        for k in outDegree:
            if outDegree[k] > inDegree[k]:
                start = k
                break

        if start == None:
            start = pairs[-1][-1]

        res = deque()
        def heirholtzer(node):
            while adjList[node]:
                nextNode = adjList[node].pop()
                heirholtzer(nextNode)

            res.appendleft(node)

        
        heirholtzer(start)
        output = []
        for num1, num2 in pairwise(res):
            output.append([num1, num2])
        return output