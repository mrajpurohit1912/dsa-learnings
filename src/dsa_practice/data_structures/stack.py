class Stack:
    def __init__(self):
        self.data = []

    def push(self, item: int) -> None:
        """Pushes an element onto the stack."""
        self.data.append(item)

    def pop(self) -> int:
        """Pops the top element from the stack. Raises IndexError if empty."""
        if not self.data:
            raise IndexError("pop from empty stack")
        return self.data.pop()
    
    def peek(self) -> int:
        """Returns the top element of the stack without removing it."""
        if not self.data:
            raise IndexError("peek from empty stack")
        return self.data[-1]

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, False otherwise."""
        return len(self.data) == 0

    def display(self) -> None:
        """Prints the stack elements."""
        print(self.data)

if __name__ == "__main__":
    print("--- Stack Demo ---")
    st = Stack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.display()
    
    print(f"Peek: {st.peek()}")
    print(f"Pop: {st.pop()}")
    print(f"Pop: {st.pop()}")
    st.display()