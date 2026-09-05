class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        stones = sorted(range(len(aliceValues)),key=lambda i: aliceValues[i] + bobValues[i],reverse=True)

        alice = bob = 0

        for turn, i in enumerate(stones):
            if turn % 2 == 0:
                alice += aliceValues[i]
            else:
                bob += bobValues[i]

        return (alice > bob) - (alice < bob)