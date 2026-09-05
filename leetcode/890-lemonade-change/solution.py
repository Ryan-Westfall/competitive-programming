class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)

        for i, bill in enumerate(bills):
            if bill == 5:
                change[bill] += 1
                continue

            if bill == 10:
                if change[5]:
                    change[10] += 1
                    change[5] -= 1
                    continue

            if bill == 20:
                if change[10] and change[5]:
                    change[10] -= 1
                    change[5] -= 1
                    change[20] += 1
                    continue

                if change[5] >= 3:
                    change[5] -= 3
                    change[20] += 1
                    continue
            return False
        return True
        


