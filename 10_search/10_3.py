class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, size, maxCollition):
        self.table = [None] * size
        self.maxCollition = maxCollition

    def hashing_function(self, key):
        return sum([ord(i) for i in list(key)])

    def insert(self, key, value):
        h = self.hashing_function(key)
        size = len(self.table)
        index = h % size
        collition = 1
        while self.table[index] is not None:
            print(f"collision number {collition} at {index}")
            if collition >= self.maxCollition:
                print("Max of collisionChain")
                print(self)
                return
            index = (h + collition**2) % size 
            collition += 1

        self.table[index] = Data(key, value)
        print(self)

        if all(self.table):
            print("This table is full !!!!!!")
            exit()
        
    def __str__(self):
        msg = ""
        n =0 
        for i in self.table:
            n += 1
            msg += "#" +  str(n) + "	" + str(i) + "\n"
        msg += "---------------------------"
        return msg
    

print(" ***** Fun with hashing *****")
table, data = input("Enter Input : ").split("/")
size, maxCollition = table.split()
h = hash(int(size), int(maxCollition))

for i in data.split(","):    
    key, value = i.split()
    h.insert(key, value)
