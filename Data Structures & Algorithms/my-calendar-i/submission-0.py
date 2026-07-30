from sortedcontainers import SortedList

class MyCalendar:
    
    def __init__(self):
        self.events = SortedList()
        

    def book(self, startTime: int, endTime: int) -> bool:
        idx = self.events.bisect_left((startTime, endTime))
        if idx > 0 and self.events[idx - 1][1] > startTime:
            return False
        if idx < len(self.events) and self.events[idx][0] < endTime:
            return False
        self.events.add((startTime, endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)