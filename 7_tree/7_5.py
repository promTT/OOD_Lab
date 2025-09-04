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
        new_node = self.Node(data)

        if self.root == None:
            self.root = new_node
            return self.root

        queue = [self.root]
        while queue:
            node = queue.pop(0)

            if node.left == None:
                node.left = new_node
                return self.root
            else:
                queue.append(node.left)

            if node.right == None:
                node.right = new_node
                return self.root
            else:
                queue.append(node.right)

    def bfs(self):
        lst = []
        queue = [self.root]
        while queue:
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            lst.append(queue.pop(0).data)
        return lst

    def switch(self, level):
        if not self.root:
            return
        queue = [(self.root, 0)]
        while queue:
            node, depth = queue.pop(0)
            if depth >= level-1:
                node.left, node.right = node.right, node.left
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

def printTreeVisual(root, indent="", last='updown'):
    if root != None:
        print(indent, end='')
        if last == 'updown': 
            print("Root----", end='')
            indent += "       "
        elif last == 'right': 
            print("R----", end='')
            indent += "       "
        elif last == 'left': 
            print("L----", end='')
            indent += "       "
        print(root.data)
        printTreeVisual(root.left, indent, 'left')
        printTreeVisual(root.right, indent, 'right')

print(" *** Mirror Tree ***")
lst, depth = input("Enter nodes in level-order,depth : ").split(",")
# s ="1 2 3 4 5 6 7,2"
# lst, depth = lst≈.split(",")

t = BST()
for i in lst.split():
    t.insert(int(i))

print(f"before mirror: {t.bfs()}")
printTreeVisual(t.root)
t.switch(int(depth))
print(f"after mirror : {t.bfs()}")
printTreeVisual(t.root)
