from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list in-place.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

# Custom Node and LinkedList implementation for local testing
class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, value: int) -> None:
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_pos(self, value: int, position: int) -> None:
        new_node = Node(value)
        if position == 0:
            self.insert_at_beg(value)
            return

        current = self.head
        position_count = 0
        prev_node = None

        while current and position_count < position:
            prev_node = current
            current = current.next
            position_count += 1

        if prev_node:
            new_node.next = current
            prev_node.next = new_node

    def reverse(self) -> None:
        """Reverses the custom linked list in-place."""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self) -> None:
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty Linked List")

if __name__ == "__main__":
    # Test custom LinkedList
    print("--- Custom LinkedList Demo ---")
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    ll.insert_at_beg(5)
    ll.insert_at_pos(15, 2)
    
    print("Original LinkedList:")
    ll.display()
    
    print("Reversed LinkedList:")
    ll.reverse()
    ll.display()

    # Test LeetCode Solution
    print("\n--- LeetCode Solution Demo ---")
    # Create standard list: 1 -> 2 -> 3
    h = ListNode(1, ListNode(2, ListNode(3)))
    sol = Solution()
    reversed_h = sol.reverseList(h)
    
    elements = []
    curr = reversed_h
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print("Reversed standard list: " + " -> ".join(elements))
