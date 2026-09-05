class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for i in nums:
            product *= i
        return self.signFunc(product)
    
    def signFunc(self,x):
        if x < 0:
            return -1
        elif x > 0:
            return 1
        else:
            return 0