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
        if self.size == 0:
            return
        return self.item.pop()
    
    
    def peek(self):
        if self.size == 0:
            return 0 
        return self.item[-1]
    
    def isEmpty(self):
        return self.item == []

    @property
    def size(self):
        return len(self.item)

    def __str__(self):
        s = "Output : "
        for ele in reversed(self.item):
            s += str(ele) + ' '
        return s
    
msg = input("Enter Input : ").split(",")
st = stack()
all_trees = []

for order in msg:
    order = order.split()
    if order[0] == "A":
        v = int(order[1])
        st.push(v)
        
    elif order[0] == "S":
        temp = stack()
        for _ in range(st.size):
            v = st.pop()
            if v % 2 == 0 and v > 1:
                v-=1
            else:
                v+=2
            temp.push(v)
        for _ in range(temp.size):
            st.push(temp.pop())
            
    elif order[0] == "B":
        see = 1
        temp = st.pop()
        for i in range(st.size):
            if temp <= st.peek():
                see+=1
                temp=st.pop()
            else:
                st.pop()

        print(see)
