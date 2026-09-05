class MyCalendar:

    def __init__(self):
        self.schedule = []

    def book(self, start: int, end: int) -> bool:
        if not self.schedule:
            self.schedule.append([start,end])
            return True
        for segment in self.schedule:
            if start < segment[0] and end <= segment[0] or start >= segment[1] and end >= segment[1] or not segment:
                pass
            else:
                return False
        self.schedule.append([start,end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)