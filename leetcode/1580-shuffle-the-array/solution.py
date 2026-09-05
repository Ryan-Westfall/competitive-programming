class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answer = []
        i = 0
        j = 0
        while i < n:
            if len(answer) % 2 == 0:
                answer.append(nums[i])
                i += 1
            else:
                answer.append(nums[n+j])
                j += 1


        return answer + [nums[-1]]