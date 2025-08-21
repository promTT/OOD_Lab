class Queue:
    def __init__(self):
        self.item = []
    
    def enQ(self, i):
        self.item.append(i)
    
    def deQ(self):
        if self.size == 0:
            return -1
        return self.item.pop(0)
    
    def peek(self):
        if self.size == 0:
            return -1
        return self.item[0]
    
    @property
    def size(self):
        return len(self.item)
    
    def __str__(self):
        return str([str(i) for i in self.item])

msg = input("Enter Input : ").split(",")

q = Queue()
qs = Queue()
for order in msg:
    order = order.split()
    if order[0] == "EN":
        q.enQ(int(order[1]))
    elif order[0] == "ES":
        qs.enQ(int(order[1]))
        
    elif order[0] == "D":
            
        if q.peek() == -1 and qs.peek() == -1:
            print("Empty")
        elif qs.peek() != -1:
            print(qs.deQ())
        else:
            print(q.deQ())