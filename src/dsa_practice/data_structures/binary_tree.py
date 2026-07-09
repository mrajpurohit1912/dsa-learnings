class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def add_data(self,data):
        if self.data == data:
            return 
        
        if self.data > data:
            if self.left:
                self.left.add_data(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            if self.right:
                self.right.add_data(data)
            else:
                self.right = BinaryTreeNode(data)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.data)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        
        print(self.data)
        if self.left:
            self.left.preorder_traversal()
        
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        
        
        if self.left:
            self.left.postorder_traversal()
        
        if self.right:
            self.right.postorder_traversal()

        print(self.data)


if __name__ == "__main__":


    values = [17, 4, 1, 20, 9, 23, 18, 34]

    root_node = BinaryTreeNode(values[0])

    for i in values[1:]:
        root_node.add_data(i)

    root_node.preorder_traversal()