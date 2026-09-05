class SparseVector:
    def __init__(self, nums: List[int]):
        self.map = {i: nums[i] for i in range(len(nums)) if nums[i]}
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        dotProductSum = 0
        for i, v in self.map.items():
            if i in vec.map:
                dotProductSum += (vec.map[i] * v)

        return dotProductSum

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)