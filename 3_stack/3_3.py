class stack:
    total = 0
    def __init__(self, item = None):
        self.item = []
        if item != None:
            item = list(item)
            for i in item:
                if i != 0:
                    self.item.append(i)
        stack.total += 1
    
    def push(self, i):
        self.item.append(i)
        return self.item
    
    def pop(self):
        if self.size() == 0:
            return
        return self.item.pop()
    
    def peek(self):
        if self.size() == 0:
            return 0 
        return self.item[-1]

    def size(self):
        return len(self.item)

    def __str__(self):
        return str(self.item)

msg = input("Enter Input : ").split("/")
lstHp = [int(i) for i in msg[0].split()]
st = stack(lstHp)
print()
print("start")
print(st)

for order in msg[1].split(","):
    order = order.split()
    if int(order[1]) <= 0:
        print()
        print("Invalid number")
        quit()
    
    if order[0] == "spawn":
        st.push(int(order[1]))
        print()
        print(f"spawn an enemy of {int(order[1])} HP")
        print(st)
    elif order[0] == "dmg":
        dmg = int(order[1])
        t = 0
        while dmg > 0 and st.size() != 0:
            dmg -= st.pop()
            if dmg >= 0:
                t += 1

        if dmg < 0:
            st.push(abs(dmg))
        print()
        print(f"deal {int(order[1])} damage, killed {t} enemy")
        print(st)
    
    if st.size() == 0:
        print()
        print(">>>> Player Wins <<<<")