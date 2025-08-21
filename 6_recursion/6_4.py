def show(data):
    for i in data:
        print("".join(map(str, i)))

def water_flow(data, col, row):
    h = data[col][row]

    data[col][row] = 0
    
    if 0 <= col+1 < len(data) and 0 <= row < len(data[0]) and h >= data[col+1][row] and data[col+1][row] != 0:
        water_flow(data, col+1, row) 
        
    if 0 <= col-1 < len(data) and 0 <= row < len(data[0]) and h >= data[col-1][row] and data[col-1][row] != 0:
        water_flow(data, col-1, row) 
        
    if 0 <= col < len(data) and 0 <= row+1 < len(data[0]) and h >= data[col][row+1] and data[col][row+1] != 0:
        water_flow(data, col, row+1) 
        
    if 0 <= col < len(data) and 0 <= row-1 < len(data[0]) and h >= data[col][row-1] and data[col][row-1] != 0:
        water_flow(data, col, row-1) 

print(" *** Water Flow ***")
size, data, start_water = input("Input rows,cols/data1,data2,.../start_row,start_col : ").split("/")
size = size.split(",")
size[0] = int(size[0])
size[1] = int(size[1])
if  size[0] not in range(1,10) or size[0] not in range(1,10):
    print("Error: Rows and columns must be between 1 and 9")
    quit()
data = data.split(",")
start_water = start_water.split(",")
start_water[0] = int(start_water[0])
start_water[1] = int(start_water[1])
for i in range(size[0]):
    data[i] = list(data[i])
    for j in range(size[1]):
        data[i][j] = int(data[i][j])

if  start_water[0] not in range(0, len(data)) or start_water[1] not in range(0, len(data[0])) :
    print("Error: Start coordinates are out of grid bounds")
    quit()

water_flow(data, start_water[0], start_water[1])
show(data)
