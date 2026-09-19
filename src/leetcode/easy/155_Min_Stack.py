class MinStack:

    def __init__(self):
        self.stack = []
        self.min_value = None
        

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append((value,value))
        else:
            min_value = min(value,self.stack[-1][1])

            self.stack.append((value,min_value))

    def pop(self) -> None:
        if not self.stack:
            raise "Stack is empty"
        self.stack.pop()

    def top(self) -> int:
        if not self.stack:
            raise "Stack is empty"
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        if not self.stack:
            raise "Stack is empty"
        return self.stack[-1][1]
        
if __name__ == "__main__":
# obj = MinStack()
# obj.push(value)
# obj.pop()

