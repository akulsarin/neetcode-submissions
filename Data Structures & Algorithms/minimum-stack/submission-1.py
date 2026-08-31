class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        min_idx = self.stack[-1][1] if self.stack else 0
        if self.stack and val < self.stack[min_idx][0]:
            min_idx = len(self.stack)
        self.stack.append((val, min_idx))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        min_idx = self.stack[-1][1]
        return self.stack[min_idx][0]
        
