class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = [[nums1[0] + nums2[0], 0, 0]]
        visited = set((0,0))
        output = []
        
        while heap and k:
            _, i1, i2 = heappop(heap)
            output.append([nums1[i1], nums2[i2]])
            k -= 1
            next_i = i1 + 1
            if next_i < len(nums1) and (next_i, i2) not in visited:
                heappush(heap, [nums1[next_i] + nums2[i2], next_i, i2])
                visited.add((next_i, i2))
            next_i = i2 + 1
            if next_i < len(nums2) and (i1, next_i) not in visited:
                heappush(heap, [nums1[i1] + nums2[next_i], i1, next_i])
                visited.add((i1, next_i))

        return output



        return output


