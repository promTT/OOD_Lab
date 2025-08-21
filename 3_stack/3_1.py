class stack:
    total = 0
    def __init__(self, item = None):
        if item == None:
            self.item = []
        else:
            self.item = item
        stack.total += 1
    
    def push(self, i):
        self.item.append(i)
        return self.item
    
    def pop(self):
        return self.item.pop()
    
    def peek(self):
        return self.item[-1]
    
    def isEmpty(self):
        return self.item == []

    def size(self):
        return len(self.item)

    def __str__(self):
        s = "Output : "
        for ele in reversed(self.item):
            s += str(ele) + ' '
        return s

print("***Always 5 or 10***")
lst = input("Enter Input : ").split()
lst = [int(i) for i in lst]

start = stack(lst)
ans = stack()
ans.push(start.pop())


while not start.isEmpty():
    if ans.peek() + start.peek() != 10 and abs(ans.peek() - start.peek()) != 10 and ans.peek() + start.peek() != 5 and abs(ans.peek() - start.peek()) != 5:
        start.pop()
    else:
        ans.push(start.pop())

print(ans)