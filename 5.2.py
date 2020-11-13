import math

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

        def createBalancedTree(self, data):
            return self.BalancedTree(data, 0, len(data)-1)

        def BalancedTree(self, data, start, end):
            if end < start:
                return None
            mid = math.floor((start+end)/2)
            tree = Tree(data[mid])
            tree.left = self.BalancedTree(data, start, mid - 1)
            tree.right = self.BalancedTree(data, mid + 1, end) 
            return tree

        def createlist(self, root):
            res = []
            if root:
                res = self.createlist(root.left)
                res.append(root.data)
                res = res + self.createlist(root.right)
            return res


        def PrintTree(self):
            if self.left:
                print(f"Вершина {self.data}")
                print(f"Лево {self.left.data}")
                self.left.PrintTree()
            if self.right:
                print(f"Вершина {self.data}")
                print(f"Право {self.right.data}")
                self.right.PrintTree()

    root = Node(8)
    root.insert(1)
    root.insert(4)
    root.insert(5)
    root.insert(10)
    root.insert(14)
    root.insert(15)
    root.insert(18)
    root.insert(3)
    listTree = root.createlist(root)
    Balance = root.createBalancedTree(listTree)
    print(Balance.PrintTree())
    

main()    
    
    
    
    