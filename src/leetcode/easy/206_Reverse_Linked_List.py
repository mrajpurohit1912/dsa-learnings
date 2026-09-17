class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        previous = None
        current = head

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        return previous


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

    sl = solution.reverseList(first_node)


    while sl:
        print(sl.val)
        sl = sl.next