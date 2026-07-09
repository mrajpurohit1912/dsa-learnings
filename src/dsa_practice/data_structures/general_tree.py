class GeneralTreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
    
    def add_child(self,data):
        self.children.append(data)

    def display(self,level=0):
        print(("-" * level * 2)  +self.data)
        for child in self.children:
            child.display(level + 1)

if __name__ == "__main__":
    electronics = GeneralTreeNode("Electronics")
    mobile = GeneralTreeNode("Mobile")
    laptop = GeneralTreeNode("Laptop")

    electronics.add_child(mobile)
    electronics.add_child(laptop)

    samsung = GeneralTreeNode("samsung")
    iphone = GeneralTreeNode("iphone")
    xi = GeneralTreeNode("xi")

    mobile.add_child(samsung)
    mobile.add_child(iphone)
    mobile.add_child(xi)


    lg = GeneralTreeNode("lg")
    acer = GeneralTreeNode("acer")
    macbook = GeneralTreeNode("macbook")

    laptop.add_child(lg)
    laptop.add_child(acer)
    laptop.add_child(macbook)


    electronics.display()