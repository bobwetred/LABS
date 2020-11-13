
def main():

    class Tree:

        def __init__(self, data):

            self.left = None
            self.right = None
            self.data = data
            
        def insert(self, data):

            if self.data:
                if data < self.data:
                    if self.left is None:
                        self.left = Tree(data)
                    else:
                        self.left.insert(data)
                elif data > self.data:
                    if self.right is None:
                        self.right = Tree(data)
                    else:
                        self.right.insert(data)
            else:
                self.data = data

        def PrintTree(self):
            if self.left:
                print(f"Вершина {self.data}")
                print(f"Левая ветвь {self.left.data}")
                self.left.PrintTree()
            if self.right:
                print(f"Вершина {self.data}")
                print(f"Правая ветвь {self.right.data}")
                self.right.PrintTree()


    root = Tree(15)
    root.insert(0)
    root.insert(8)
    root.insert(16)
    root.insert(11)
    root.insert(20)
    root.insert(1)
    root.insert(36)
    root.insert(3)
    root.insert(44)
    root.insert(5)

    print(root.PrintTree())
    
main()    