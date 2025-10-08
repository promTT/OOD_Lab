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

    def postOrder(self):
        result = " ".join(self._postOrder(self.root))
        print(f"AVLTree post-order : {result}")
        

    def _postOrder(self, root):
        if root is None:
            return []
        return self._postOrder(root.left) + self._postOrder(root.right) + [str(root.data)]


    def printTree(self):
        AVLTree._printTree(self.root)
        print()

    def _printTree(node , level=0):
        if not node is None:
            AVLTree._printTree(node.right, level + 1)
            print('     ' * level, node.data)
            AVLTree._printTree(node.left, level + 1)


avl1 = AVLTree()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AD":
        avl1.add(int(i[3:]))
    elif i[:2] == "PR":
        avl1.printTree()
    elif i[:2] == "PO":
        avl1.postOrder()