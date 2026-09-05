class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = collections.Counter(nums)

        heap = []

        for key, v in counter.items():
            heap.append((-v, key))

        heapq.heapify(heap)

        result = []


        while k:
            result.append(heapq.heappop(heap)[1])
            k -= 1

        return result

