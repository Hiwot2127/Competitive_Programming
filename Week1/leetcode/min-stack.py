class MinStack:

    def __init__(self):
        self.stack= []
        self.mStack= []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mStack or val<= self.mStack[-1]:
            self.mStack.append(val)
        
    def pop(self) -> None:
        if self.mStack[-1]==self.stack[-1]:
            self.mStack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()