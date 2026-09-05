class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        currentBytes = 0
        for num in data:
            binary = format(num, '08b')
            if currentBytes:
                if binary[:2] != '10':
                    return False
                currentBytes -= 1
            else:
                for i, bit in enumerate(binary):
                    if i == 0 and bit == '0':
                        break
                    if i == 1 and bit == '0':
                        print('hit2')
                        return False
                    if i == 2 and bit == '0':
                        currentBytes = 1
                        break
                    if i == 3 and bit == '0':
                        currentBytes = 2
                        break
                    if i == 4 and bit == '0':
                        currentBytes = 3
                        break
                    if i == 5:
                        return False

        return not currentBytes
        