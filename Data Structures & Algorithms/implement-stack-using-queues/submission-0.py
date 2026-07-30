from collections import deque

class MyStack:

    def __init__(self):
        self.primary = deque()
        self.secondary = deque()
        

    def push(self, x: int) -> None:
        self.primary.append(x)
        

    def pop(self) -> int:
        while len(self.primary) > 1:
            el = self.primary.popleft()
            self.secondary.append(el)
        
        res = self.primary.popleft()
        self.primary, self.secondary = self.secondary, self.primary
        return res
        

    def top(self) -> int:
        res = self.pop()
        self.primary.append(res)
        return res

        
    def empty(self) -> bool:
        return len(self.primary) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()