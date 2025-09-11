class AVLTree:
    class AVLNode:
        def __init__(self, data, left = None, right = None):
            self.data = data
            self.left = None if left is None else left
            self.right = None if right is None else right
            self.height = self.setHeight()
        
        def __str__(self):
            return str(self.data)
        
        def setHeight(self):
                a = self.getHeight(self.left)
                b = self.getHeight(self.right)
                self.height = 1 + max(a,b)
                return self.height
        
        def getHeight(self, node):
            return -1 if node == None else node.height
        
        def balanceValue(self):      
            return self.getHeight(self.left) - self.getHeight(self.right)


    def __init__(self, root = None):
        self.root = None if root is None else root
        
    def add(self, data):
        self.root = self._add(self.root, data)

    def _add(self, root, data):
        if root == None:
            return self.AVLNode(data)
        else:
            if data < root.data:
                root.left = self._add(root.left, data)
            else:
                root.right = self._add(root.right, data)
        root.setHeight()
        root = self.rebalance(root)
        return root

    def rebalance(self, x):
        if x is None:
            return x
        balance = x.balanceValue()

        if balance == -2:
            if x.right.balanceValue() > 0:
                x.right = self.rightRotate(x.right)
            x = self.leftRotate(x)

        elif balance == 2:
            if x.left.balanceValue() < 0:
                x.left = self.leftRotate(x.left)
            x = self.rightRotate(x)

        x.setHeight()
        return x

    def leftRotate(self, root):
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot

    def rightRotate(self, root):
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.setHeight()
        newRoot.setHeight()
        return newRoot
    
    def printTree(self):
        self._printTree(self.root, 0)

    def printTree(self, node , level=0):
        if not node is None:
            self.printTree(node.right, level + 1)
            print('     ' * level , str(node.data))
            self.printTree(node.left, level + 1)
            

    def __str__(self):
        self.printTree(self.root)

    def getApple(self):
        if not self.root:
            return []
        
        stack = [(self.root, [self.root.data])]
        best_path = []
        
        while stack:
            current, path = stack.pop()
            if sum(path) > sum(best_path):
                best_path = path[:]
            if current.right:
                stack.append((current.right, path + [current.right.data]))
            if current.left:
                stack.append((current.left, path + [current.left.data]))
        return best_path

t = AVLTree()

Tree1_inp = (input("Enter tree nodes: "))

for data in Tree1_inp.split():
    t.add(int(data))

t.printTree(t.root)
print()
path = t.getApple()
s = " + ".join([str(i) for i in path])
print(f"Path with maximum sum: {s} = {sum(path)}")