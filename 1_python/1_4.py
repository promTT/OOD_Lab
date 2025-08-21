print("*** Minesweeper ***")

def num_grid(lst):
    for y in range(len(lst)-1):
        for x in range(len(lst[y])-1):
            if lst[y][x] == "-" and x <= 5 and x >= 1 and y <= 5 and y >= 1:
                around = 0
                if lst[y][x+1] == "#":
                    around+=1
                if lst[y][x-1] == "#":
                    around+=1
                if lst[y+1][x] == "#":
                    around+=1
                if lst[y-1][x] == "#":
                    around+=1
                if lst[y+1][x+1] == "#":
                    around+=1
                if lst[y-1][x-1] == "#":
                    around+=1
                if lst[y+1][x-1] == "#":
                    around+=1
                if lst[y-1][x+1] == "#":
                    around+=1
                lst[y][x] = str(around)
                
                
    lst_input.pop(0)
    lst_input.pop(5)
    for e in lst_input:
        e.pop(0)
        e.pop(5)
    return lst



'''lst_input = [

    ["-","-","-","-","-"],

    ["-","-","-","-","-"],

    ["-","-","#","-","-"],

    ["-","-","-","-","-"],

    ["-","-","-","-","-"]

]'''

lst_input = []

input_list = input("Enter input(5x5) : ").split(",")

for e in input_list:
  lst_input.append([i for i in e.split()])

print("\n",*lst_input,sep = "\n")

lst_input.insert(0, ["x","x","x","x","x"])
lst_input.append(["x","x","x","x","x", ])
for e in lst_input:
    e.insert(0, "x")
    e.append("x")


print("\n",*num_grid(lst_input),sep = "\n")

