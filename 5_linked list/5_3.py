class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            
        def __str__(self):
            return str(self.data)
        
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
    
    def swap(self, preNodeA ,nodeA, nodeB):
        temp = None
        if nodeB != self.tail:
            temp = nodeB.next
        if nodeA != self.head:
            preNodeA.next = nodeB
        else:
            self.head = nodeB
        nodeB.next = nodeA
        nodeA.next = temp
        if temp == None:
            self.tail = nodeA
        print(f"{self}")
    
    def findByIndex(self, index):
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    def __str__(self):
        ans = []
        node = self.head
        while node:
            ans.append(str(node))
            node = node.next
        return ' -> '.join(ans)
    

lst = LinkedList()
inp = input("input : ").split()

for i in inp:
    lst.append(i)
    
print(f"Original\n{lst}")

print("\nProcess")

for n in range(lst.size - 1, 0, -1):
    beforeCurrent = None
    current = lst.head
    for i in range(n):
        lst.swap(beforeCurrent, current, current.next)
            
        if beforeCurrent == None:
            beforeCurrent = lst.head
        else:
            beforeCurrent = beforeCurrent.next

print(f"\nReverse\n{lst}")