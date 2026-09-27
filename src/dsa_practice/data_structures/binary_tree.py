# class BinaryTreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def add_data(self,data):
#         if self.data == data:
#             return 
        
#         if self.data > data:
#             if self.left:
#                 self.left.add_data(data)
#             else:
#                 self.left = BinaryTreeNode(data)
#         else:
#             if self.right:
#                 self.right.add_data(data)
#             else:
#                 self.right = BinaryTreeNode(data)

#     def inorder_traversal(self):
#         if self.left:
#             self.left.inorder_traversal()
#         print(self.data)
#         if self.right:
#             self.right.inorder_traversal()

#     def preorder_traversal(self):
        
#         print(self.data)
#         if self.left:
#             self.left.preorder_traversal()
        
#         if self.right:
#             self.right.preorder_traversal()

#     def postorder_traversal(self):
        
        
#         if self.left:
#             self.left.postorder_traversal()
        
#         if self.right:
#             self.right.postorder_traversal()

#         print(self.data)


# if __name__ == "__main__":


#     values = [17, 4, 1, 20, 9, 23, 18, 34]

#     root_node = BinaryTreeNode(values[0])

#     for i in values[1:]:
#         root_node.add_data(i)

#     root_node.preorder_traversal()


from collections import deque

class BinaryTreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self,root_node: BinaryTreeNode) -> None:
        self.root_node = root_node


    def get_root_node(self):
        return self.root_node if self.root_node else None

    def build_binary_tree(self,val):
        new_node = BinaryTreeNode(val)
        
        if not self.root_node:
            self.root_node = new_node
            return


        queue = deque([self.root_node])

        while queue:
            current = queue.popleft()

            if current.left is None:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.right)