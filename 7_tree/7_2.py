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

    def printTree(self, node):
        print(self._printTree(node))

    def _printTree(self, node, level=0):
        if node is None:
            return ""
        result = self._printTree(node.right, level + 1)
        result += " " * 4 * level + f"{node.data}\n"
        result += self._printTree(node.left, level + 1)
        return result
    
    def bfs(self, node):
        lst = []
        queue = [node]
        while queue:
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            lst.append(queue.pop(0).data)
        return lst

    def dfs(self, node):
        lst = []
        stack = [node]
        visited = set()
        while stack:
            current = stack.pop()
            if current not in visited:
                lst.append(current.data)
                visited.add(current)
                if current.left:
                    stack.append(current.left)
                if current.right:
                    stack.append(current.right)
        return lst


print("******BFS Pis-sa-dan******")
T = BST()
inp = [int(i) for i in input('Enter numbers: ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print(f"BFS: {T.bfs(root)}")
print(f"BFS Pid-Sa-Dan: {T.dfs(root)}")