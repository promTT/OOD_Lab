class stack:
    total = 0
    plate = [25, 20, 15, 10, 5, 2.5, 1.25]
    def __init__(self, item = None):
        if item == None:
            self.item = []
        else:
            self.item = item
            
        self.logpo = []
        self.logpu = []
        stack.total += 1
    
    def push(self, item):
        if self.size == 5:
            return "no room"
        if self.size > 0:
            if self.item[-1] < item:
                return "plate error"            
        
        self.item.append(item)
        self.logpu.append(item)
        return self.item
    
    def pop(self):
        self.logpo.append(self.item[-1])
        return self.item.pop()
    
    def peek(self):
        return self.item[-1]
    
    def isEmpty(self):
        return self.item == []

    @property
    def size(self):
        return len(self.item)

    @property
    def totalWeight(self):
        weight = 20
        weight += sum(self.item)*2
        return weight

    def want(self, target):
        temp = []
        oldTarget = target
        target -= 20
        for i in stack.plate:
            while target >= i*2:
                temp.append(i)
                target -= i*2
        
        if target != 0 or len(temp) > 5:
            if float(oldTarget).is_integer():
                oldTarget = int(oldTarget)
            else:
                oldTarget = float(oldTarget)
            print(f"It's impossible to achieve the weight you want({oldTarget}).")
            quit()
        
        temp.sort(reverse=True)
        
        if len(temp) < len(self.item):
            for _ in range(len(self.item) - len(temp)):
                self.pop()

        # print(self.item)
        haveChange = False
        for i in range(min(len(self.item), len(temp))):
            # print(i)
            if self.item[i] == temp[i] and haveChange:
                    self.logpo.append(self.item[i])
                    self.logpu.append(temp[i])
            
            if self.item[i] != temp[i]:
                # print(self.item[i])
                # print(temp[i])
                self.logpo.append(self.item[i])
                self.logpu.append(temp[i])
                self.item[i] = temp[i]
                haveChange = True
            
            
        for i in range(len(self.item), len(temp)):
            self.push(temp[i])
        
        return self.item

    def __str__(self):
        msg = ""
        
        self.logpu.sort(reverse=True)
        self.logpo.sort()
        
        for log in self.logpo:
            msg += f"PO:{log} "
        
        for log in self.logpu:
            msg += f"PU:{log} "
            
        if len(self.logpo) > 0 or len(self.logpu) > 0:
            msg += "=> "
        
        msg += "-" * (5 - self.size)
        for ele in reversed(self.item):
            msg += "[" + str(ele) + "]"
            
        msg += "|======|"
        
        for ele in self.item:
            msg += "[" + str(ele) + "]"
        msg += "-" * (5 - self.size)

        msg += " => "+ str(self.totalWeight) + " KG."
        self.logpo = []
        self.logpu = []
        
        return msg

q = [float(i) for i in input("Enter needed weight(s): ").split()]
bar = stack()

for i in q:
    bar.want(i)
    print(bar)