class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        numberline = [];
        for number in range(1,n+1):
            print(number)
            if number % 5 == 0 and number % 3 == 0:
                numberline.append("FizzBuzz")    
            elif number % 3 == 0:
                numberline.append("Fizz") 
            elif number % 5 == 0:
                numberline.append("Buzz")
            else:
                numberline.append(str(number))
        return numberline
                
        