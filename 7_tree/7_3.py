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
            if data > node.data:
                node.right = self._insert(node.right, data)
        return node

    def update(self, k):
        queue = [self.root]
        while queue:
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            n = queue.pop(0)
            if n.data > k:
                n.data *= k

    def sum(self):
        queue = [self.root]
        s = 0
        while queue:
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            s += queue.pop(0).data
        return s
    
    def printTree(self, node = "a",level = 0):
        if node == "a" :
            node = self.root
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)


print("**Sum of tree**")
lst, k = input('Enter input : ').split("/")
lst = [int(i) for i in lst.split()]
before_Tree = BST()
for i in lst:
    before_Tree.insert(i)

print("\nTree before:")
before_Tree.printTree()
print(f"Sum of all nodes = {before_Tree.sum()}")
before_Tree.update(int(k))
print("\nTree after: ")
before_Tree.printTree()
print(f"Sum of all nodes = {before_Tree.sum()}")