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
for order in msg:
    order = order.split()
    if order[0] == "E":
        q.enQ(int(order[1]))
        print(f"Add {int(order[1])} index is {q.size - 1}")
    elif order[0] == "D":
        if q.peek() == -1:
            print("-1")
        else:
            print(f"Pop {q.deQ()} size in queue is {q.size}")
if q.size == 0:
    print("Empty")
else:
    print(f"Number in Queue is :  {q}")