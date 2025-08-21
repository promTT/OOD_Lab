class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.type = "Army" if data.startswith("A") else "Worker"
            self.next = None
            
        def __str__(self):
            return str(self.data)
        
    def __init__(self):
        self.head = None
        self.size = 0
    
    A = 0
    def appendArmy(self):
        LinkedList.A+=1
        if self.size > 0:
            if self.armyTail:
                self.armyTail.next = self.Node(f"A{LinkedList.A}")
            elif self.workerTail:
                self.workerTail.next = self.Node(f"A{LinkedList.A}")
            else:
                self.head = self.Node(f"A{LinkedList.A}")
        else:
            self.head = self.Node(f"A{LinkedList.A}")
        self.size += 1
        # if self.size > 1:
        #     self.sort()
    
    W = 0
    #can by cause of hidden case
    def appendWorker(self):
        LinkedList.W+=1
        if self.size > 0:
            if LinkedList.W > 1:
                self.workerTail.next = self.Node(f"W{LinkedList.W}")
            else:
                self.armyTail.next = self.Node(f"W{LinkedList.W}")
        else:
            self.head = self.Node(f"W{LinkedList.W}")
        self.size += 1
        # if self.size > 1:
            # self.sort()
    
    def remove(self, item):
        if item.type == "Army":
            LinkedList.A -= 1
        else:
            LinkedList.W -= 1
            
        node = self.head
        if node.data == item.data:
            self.head = node.next
            self.size -= 1
            return "success"
        while node.next:
            if node.next.data == item.data:
                node.next = item.next
                self.size -= 1
                return "success"
            else:
                node = node.next
        return "can't find"
    
    def findByIndex(self, index):
        node = self.head
        for _ in range(index):
            node = node.next
        return node
    
    @property
    def armyHead(self):
        return self.workerTail.next if self.workerTail else None
    
    @property
    def workerTail(self):
        node = self.head

        if not node:
            return None

        while node:
            if node.type == "Worker":
                if not node.next or node.next.type == "Army":
                    return node
                if node.next.type == "Worker":
                    if not node.next.next or node.next.next.type == "Army":
                        return node.next
            node = node.next

        return None
    
    @property
    def armyTail(self):
        node = self.head
        last_army = None

        while node:
            if node.type == "Army":
                last_army = node
            node = node.next

        return last_army
    
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
    
    # def sort(self):
    #     for n in range(self.size - 1, 0, -1):
    #         current = self.head
    #         swapped = False  
    #         beforeCurrent = None
    #         while current:
    #             (current)
    #             if current.type == current.next.type and current.data[1:] > current.next.data[1:]:
    #                 self.swap(beforeCurrent, current, current.next)
    #                 swapped = True
    #             else:
    #                 current = current.next
    #             if beforeCurrent == None:
    #                 beforeCurrent = self.head
    #             else:
    #                 beforeCurrent = beforeCurrent.next
    #         if not swapped:
    #             break

    def __str__(self):        
        ans = "-> Remaining worker ants:"
        node = self.head
        if node and node.type == "Worker":
            while node and node.type == "Worker":
                ans += " "
                ans += node.data
                node = node.next
        else:
            ans += " Empty"
        
        ans += "\n"
        
        ans += "-> Remaining soldier ants:"
        if node:
            while node:
                ans += " "
                ans += node.data
                node = node.next
        else:
            ans += " Empty"
        
        return ans

print("***This colony is our home***")
ant, order = input("Enter input : ").split("/")
anger = 0
colony = LinkedList()

worker, army = ant.split()
for _ in range(int(worker)):
    colony.appendWorker()
for _ in range(int(army)):
    colony.appendArmy()

print("Current Ant List:", end="")
ant = colony.head
if ant != None:
    while ant:
        print(f" {ant}",end="")
        ant = ant.next
    print("\n")
else:
    print(" Empty\n")



for command in order.split(","):
    parts = command.split()
    if len(parts) == 2:
        command, amount = parts
        amount = int(amount)
    else:
        command = parts[0]
        amount = None
    
    if command == "C":
        ant = colony.head
        print("Food carrying mission :", end="")
        
        if isinstance(ant, LinkedList.Node):
            while amount > 0 and ant != None:
                if ant.type == "Worker":
                    amount -= 2
                else:
                    amount -= 5
                print(f" {ant}", end="")
                colony.remove(ant)
                ant = ant.next
        else:
            print(" Empty", end="")
        print()
    
        if amount > 0:
            print("The food load is incomplete!\nQueen is angry! ! !")
            anger += 1
            if anger >= 3:
                print("**The queen is furious! The ant colony has been destroyed**")
                quit()
    
    elif command == "F":
        ant = colony.armyHead
        print("Attack mission :", end="")
        
        while amount > 0 and ant != None:
            if ant.type == "Army":
                amount -= 10
            else:
                amount -= 5
            print(f" {ant}", end="")
            colony.remove(ant)
            ant = ant.next
        
        ant = colony.head
        while amount > 0 and ant != colony.armyHead:
            if ant.type == "Army":
                amount -= 10
            else:
                amount -= 5
            print(f" {ant}", end="")
            colony.remove(ant)
            ant = ant.next
            
        if amount > 0:
            print()
            print("Ant nest has fallen!")
            quit()
        else:
            print()
    
    elif command == "S":
        print(colony)
    
    elif command == "A":
        for _ in range(amount):
            colony.appendArmy()
    
    elif command == "W":
        for _ in range(amount):
            colony.appendWorker()