class Solution:
    def reverse(self, x: int) -> int:
        numbers = []
        negative = False
        if x < 0:
            negative = True
            x = abs(x)
        check = False
        for i in range(len(str(x))-1, -1, -1):
            if not check and str(x)[i] == 0:
                pass
            else:
                check = True
                numbers.append(str(x)[i])
        numbers = ''.join(numbers)
        numbers = int(numbers)
        if negative:
            numbers *= -1
        if numbers < -2147483648 or numbers > 2147483647:
            return 0
        return numbers
                
            