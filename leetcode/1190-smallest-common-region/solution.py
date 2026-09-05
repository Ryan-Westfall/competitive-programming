class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        adjListUp = defaultdict(list)

        for region in regions:
            src = region[0]
            for dstIndex in range(1, len(region)):
                adjListUp[region[dstIndex]].append(src)

        queue = deque([region1, region2])
        visit = set()
        while queue:
            node = queue.popleft()
            if node in visit:
                return node
            visit.add(node)
            for nei in adjListUp[node]:
                queue.append(nei)
