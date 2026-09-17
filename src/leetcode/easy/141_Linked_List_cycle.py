from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 

            if slow == fast:
                return True

        return False

if __name__ == "__main__":
    solution = Solution()
    first_node = ListNode(2)
    second_node = ListNode(3)
    third_node = ListNode(8)
    fourth_node = ListNode(19)
    fifth_node = ListNode(23)

    first_node.next =second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = fifth_node

    sl = solution.hasCycle(first_node)

    print(sl)