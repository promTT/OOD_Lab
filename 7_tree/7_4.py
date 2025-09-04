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
    
    def printTree(self, node = "a",level = 0):
        if node == "a" :
            node = self.root
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def printPath(self, path):
        print("❌ " + " -> ".join(str(node) for node in path))
    
    def findTreasure(self, treasure):
        stack = [(self.root, [self.root])]
        while stack:
            temp = stack[:]
            current, path = stack.pop()

            if current.data == treasure:
                print("Found Treasure !!!")
                return temp
            self.printPath(path)
            if current.right:
                stack.append((current.right, path + [current.right]))
            if current.left:
                stack.append((current.left, path + [current.left]))

        print(">>> Mission Failed <<<")
        quit()
        return []
    
    def findTreasureAndEscape(self, treasure, escape):
        stack = self.findTreasure(treasure)
        while stack:
            current, path = stack.pop()

            if current.data == escape:
                print("Found Escape !!!")
                print("✅ " + " -> ".join(str(node) for node in path))
                print(">>> Mission Complete <<<")
                return path
            self.printPath(path)
            if current.right:
                stack.append((current.right, path + [current.right]))
            if current.left:
                stack.append((current.left, path + [current.left]))

        print(">>> Mission Failed <<<")
        return []
        
lst, treasure, escape = input('Enter Input : ').split("/")
lst = [int(i) for i in lst.split()]

t = BST()
for i in lst:
    t.insert(i)
t.printTree()
print("-------------------------------------------------")
t.findTreasureAndEscape(int(treasure),int(escape))