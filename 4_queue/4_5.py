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
        result = []
        for i in self.item:
            if isinstance(i, Queue):
                result.append(str(i))
            else:
                result.append(str(i))
        return "[" + ", ".join(result) + "]"


print(" ***Queue of Queue of Queue of ...***")
orders = input("Enter Input : ").split(",")
q = Queue()
empty =False
for order in orders:
    order = order.split()
    if order[0] == "en":
        order[1] = int(order[1])
        print(f"Enqueued: {order[1]}")
        temp = Queue()
        find = False
        if q.size != 0:
            for _ in range(q.size):
                if q.peek().peek() // 100 != order[1] // 100 :
                    temp.enQ(q.deQ())
                else:
                    find = True
                    q.peek().enQ(order[1])
                    temp.enQ(q.deQ())
            for _ in range(temp.size):
                q.enQ(temp.deQ())
                
        if not find:
            org = Queue()
            org.enQ(order[1])
            q.enQ(org)
            
    elif order[0] == "de":
        if q.size == 0:
            empty=True
            print("Queue is empty")
        else:
            print(f"Dequeued: {q.peek().deQ()}")
            if q.peek().size == 0 :
                q.deQ()
    if not empty:
        print(f"Queue state: {q}")