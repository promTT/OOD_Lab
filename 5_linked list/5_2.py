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
        print()
        print(f"Swapping {nodeA} and {nodeB}")
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
        print(f"List: {self}")
    
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
        return '->'.join(ans)


print("*****Bubble Sort Linked List*****")
lst = LinkedList()
inp = input("Enter Input: ").split(",")

for i in inp:
    lst.append(int(i))
print(f"Input List: {lst}\n_______________________________________")

for n in range(lst.size - 1, 0, -1):
    # Initialize swapped to track if any swaps occur
    
    swapped = False  
    beforeCurrent = None
    # Inner loop to compare adjacent elements
    current = lst.head
    for i in range(n):
        # print(f"{current.data > current.next.data}, current.date = {current.data}")
        if current.data > current.next.data:
            # Swap elements if they are in the wrong order
            lst.swap(beforeCurrent, current, current.next)
            

            # Mark that a swap has occurred
            swapped = True
        else:
            current = current.next
        if beforeCurrent == None:
            beforeCurrent = lst.head
        else:
            beforeCurrent = beforeCurrent.next
    # If no swaps occurred, the list is already sorted
    if not swapped:
        break

print(f"_______________________________________\nSorted List: {lst}")