class Solution:

    def __init__(self, nums: List[int]):
        self.hashmap = defaultdict(list)
        for i in range(len(nums)):
            self.hashmap[nums[i]].append(i)

    def pick(self, target: int) -> int:
        # return random.randint(self.hashmap[target][0], self.hashmap[target][-1])
        return random.choice(self.hashmap[target])

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)