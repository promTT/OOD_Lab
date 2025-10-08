class Data:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class hash:
    def __init__(self, size, maxCollition, threshold):
        self.table = [None] * size
        self.maxCollition = maxCollition
        self.threshold = threshold/100

    def hashing_function(self, key):
        return int(key)

    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def prime(self, n):
        target = 2 * n
        while not self.is_prime(target):
            target += 1
        return target

    def rehash(self):
        size = len(self.table)
        newTable = [None] * self.prime(size)
        
        for data in reversed(self.table):
            if data is not None:
                self._insert(data.value, newTable)
        self.table = newTable[:]
    
    
    def _insert(self, value, t):
        h = self.hashing_function(value)
        size = len(t)
        index = h % size
        collition = 0

        while t[index] is not None:
            collition += 1
            print(f"collision number {collition} at {index}")
            index = (h + collition ** 2) % size
            # print(self)

        t[index] = Data(value)
        
    def insert(self, value):    
        print(f"Add : {value}")
        
        dataLen = 0
        for i in self.table:
            if i is not None:
                dataLen += 1
        if (dataLen+1)/len(self.table) >=self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
        
        h = self.hashing_function(value)
        size = len(self.table)
        index = h % size
        collition = 0
        
        while self.table[index] is not None:
            collition += 1
            print(f"collision number {collition} at {index}")
            if collition >= self.maxCollition:
                print("****** Max collision - Rehash !!! ******")
                self.rehash()
                self._insert(value, self.table)
                print(self)
                return
            
            index = (h + collition**2) % size 


        self.table[index] = Data(value)
        print(self)

        # if all(self.table):
        #     print("This table is full !!!!!!")
        #     exit()
        
    def __str__(self):
        msg = ""
        n =0 
        for i in self.table:
            n += 1
            msg += "#" +  str(n) + "	" + str(i) + "\n"
        msg += "----------------------------------------"
        return msg
    

print(" ***** Rehashing *****")
table, data = input("Enter Input : ").split("/")
size, maxCollition, Threshold = table.split()
h = hash(int(size), int(maxCollition), int(Threshold))
print("Initial Table :")
print(h)

for i in data.split():    
    h.insert(i)
