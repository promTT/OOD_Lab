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

goingToPass = Queue()

print("*****Hot Potato Game*****")

order, time = input("Enter Input: ").split("/")
orders = order.split(",")
time = int(time)

for item in orders:
    goingToPass.enQ(str(item))

eliminated = ""


while goingToPass.size > 1:
    eliminated = goingToPass.peek()
    print(f"{eliminated} is the first player holding the potato")
    for t in range(time):
        a = goingToPass.deQ()
        eliminated = goingToPass.peek()
        print(f"  Potato passed to: {eliminated}")
        goingToPass.enQ(a)
    goingToPass.deQ()
    print(f"Eliminated: {eliminated}. Remaining players: {goingToPass}")
    
print()
print(f"The winner is: {goingToPass.peek()}!")