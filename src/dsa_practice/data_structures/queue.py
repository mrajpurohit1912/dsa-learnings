class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, item: int) -> None:
        """Enqueues an element at the back of the queue."""
        self.data.append(item)

    def dequeue(self) -> int:
        """Dequeues the front element of the queue. Raises IndexError if empty."""
        if not self.data:
            raise IndexError("dequeue from empty queue")
        return self.data.pop(0)

    def peek(self) -> int:
        """Returns the front element of the queue without removing it."""
        if not self.data:
            raise IndexError("peek from empty queue")
        return self.data[0]

    def is_empty(self) -> bool:
        """Returns True if the queue is empty, False otherwise."""
        return len(self.data) == 0

    def display(self) -> None:
        """Prints the queue elements."""
        print(self.data)

if __name__ == "__main__":
    print("--- Queue Demo ---")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.display()
    
    print(f"Peek: {q.peek()}")
    print(f"Dequeue: {q.dequeue()}")
    print(f"Dequeue: {q.dequeue()}")
    q.display()