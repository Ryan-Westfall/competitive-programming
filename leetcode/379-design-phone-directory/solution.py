class PhoneDirectory:

    def __init__(self, maxNumbers: int):
        self.avaliable = set(i for i in range(maxNumbers))
        self.used = set()
        

    def get(self) -> int:
        if self.avaliable:
            number = self.avaliable.pop()
            self.used.add(number)
            return number
        else:
            return -1
        

    def check(self, number: int) -> bool:
        return number in self.avaliable
        

    def release(self, number: int) -> None:
        if number in self.used:
            self.used.remove(number)
            self.avaliable.add(number)
        


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)