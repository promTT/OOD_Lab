class Stack:
    def __init__(self):
        self.list = []
    
    def push(self, data):
        self.list.append(data)
    
    def pop(self):
        return self.list.pop()
    
    def peek(self):
        return self.list[-1]
    
    def isEmpty(self):
        return self.list == []

print("*****Big leg on the right side*****")
inp = list(map(int, input("Enter input: ").split()))
output = [-1] * len(inp)
stack = Stack()

for i in range(len(inp)):
    while not stack.isEmpty() and inp[i] > inp[stack.peek()]:
        index = stack.pop()
        print(f"input[{i}]({inp[i]}) is greater than input[top of stack]({inp[index]})")
        output[index] = inp[i]
        print("Stack pop")
        print(f"Output: {output}")
    print(f"Stack push {i} index of {inp[i]}")
    stack.push(i)

print(f"Output: {output}")