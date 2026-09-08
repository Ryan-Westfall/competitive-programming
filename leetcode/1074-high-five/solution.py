class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        
        scores = defaultdict(list)

        for studentId, score in items:
            heap = scores[studentId]
            heapq.heappush(heap, score)
            if len(heap) > 5:
                heapq.heappop(heap)

        res = []
        for k in scores:
            total = 0
            for score in scores[k]:
                total += score
            res.append([k, total // len(scores[k])])

        res.sort(key=lambda x: x[0])
        return res
