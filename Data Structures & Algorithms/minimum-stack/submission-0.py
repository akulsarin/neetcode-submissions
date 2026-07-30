class MinStack:

    def __init__(self):
        self.elements = []
        self.minIndices = []
        

    def push(self, val: int) -> None:
        self.elements.append(val)
        
        if len(self.elements) == 1 or val < self.getMin():
            self.minIndices.append(len(self.elements) - 1)
        

    def pop(self) -> None:
        self.elements.pop()

        if self.minIndices[-1] == len(self.elements):
            self.minIndices.pop()

        
    def top(self) -> int:
        return self.elements[-1]
        

    def getMin(self) -> int:
        return self.elements[self.minIndices[-1]]
        
