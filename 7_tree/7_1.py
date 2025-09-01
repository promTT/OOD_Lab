class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
        
        def __str__(self):
            return str(self.data)

    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root
    
    def _insert(self, node, data):
        if node == None:
            return self.Node(data)
        else:
            if data < node.data:
                node.left = self._insert(node.left, data)
            else:
                node.right = self._insert(node.right, data)
        return node

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)



T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)