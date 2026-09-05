class Solution:
    def titleToNumber(self, s: str) -> int:
        #dict to hold letter and its serial number
        LETTERS = {letter: index for index, letter in enumerate(ascii_uppercase, 1)}
		
        col_num = 0
		
		#convert the like 26-base number to decimal
        for i in range(len(s)):
            col_num += LETTERS[s[-1 - i]] * (26 ** i)
            
        return col_num
            