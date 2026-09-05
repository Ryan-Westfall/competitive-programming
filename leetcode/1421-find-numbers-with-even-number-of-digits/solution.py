class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        number = 0
        count = 0
        for i in nums:
            while i > 0:
                i = i // 10
                count+=1
            if count % 2 == 0:
                number+=1
            count = 0
        return number