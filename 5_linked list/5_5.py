class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
        
        def __str__(self):
            return self.data
            
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.size = 0

    def append(self,data):
        if self.size > 0:
            self.tail.next = self.Node(data)
            self.tail = self.tail.next
        else:
            self.head = self.Node(data)
            self.tail = self.head
        self.size += 1

    def get_node_at(self, index):
        node = self.head
        for _ in range(index):
            if node is None:
                return None
            node = node.next
        return node

    def get_prev_node(self, target):
        if target == self.head:
            return None
        node = self.head
        while node and node.next != target:
            node = node.next
        return node

    def swap(self, preNodeA ,nodeA, nodeB):
        if not nodeA or not nodeB:
            return
        temp = nodeB.next
        if preNodeA:
            preNodeA.next = nodeB
        else:
            self.head = nodeB
        nodeB.next = nodeA
        nodeA.next = temp
        if temp is None:
            self.tail = nodeA

    def reverse(self, start_index, n):
        for j in range(n - 1, 0, -1):
            A = self.get_node_at(start_index)
            for _ in range(j):
                preA = self.get_prev_node(A)
                B = A.next
                self.swap(preA, A, B)

    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node))
            node = node.next
        return ' → '.join(ans)

print(" *** Ant Army ***")
lst, n = input("Input : ").split(",")
n = int(n)
line = LinkedList()

for i in lst.split():
    line.append(i)

print(f"Before : {line}")

i = 0
if n == 0:
    pass
elif i * n + n <= line.size:
    while i * n + n <= line.size:
        if i % 2 == 0:
            line.reverse(i * n, n)
        i += 1
    if i * n <= line.size:
        if i % 2 == 0:
            line.reverse(i * n, line.size-(i*n))
else:
    line.reverse(0, line.size)

print(f"After : {line}")