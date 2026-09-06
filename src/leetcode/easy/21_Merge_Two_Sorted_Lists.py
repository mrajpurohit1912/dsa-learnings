from typing import List,Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode()

        current_node = dummy_node

        while list1 and list2:

            if list1.val <= list2.val:
                current_node.next = list1.val
                list1 = list1.next

            else:
                current_node.next = list2.val
                list2 = list2.next

            current_node = current_node.next

        current_node.next = list1 if list1 else list2


        return dummy_node.next


if __name__ == "__main__":
    list1 = [1,2,4]
    list2 = [1,3,4]

    sl = Solution()
    print(sl.mergeTwoLists(list1,list2))

    # node_0 = ListNode(list1[0])
    # node_1 = ListNode(list1[1])
    # node_2 = ListNode(list1[2])

    # node_0.next =node_1
    # node_1.next =node_2


    # print(node_0.display())

    # dummy_node = ListNode(list1[0])
    # current = dummy_node

    # for val in list1[1:]:
    #     current.next = ListNode(val=val)
    #     current = current.next


    # head_node = dummy_node

    # print(head_node.val)
    # print(head_node.next)


    # print(f"Printing the data of Linked List")

    # current_node = head_node

    # while current_node:
    #     print(current_node.val)
    #     current_node = current_node.next