print("*** Fun with countdown ***")
lst = [int(c) for c in input("Enter List : ").split(" ")]
ans = [0 , []]
connect = False
count = 0
temp = []

if lst[0] == 1:
        count += 1
        temp.append(1)
        ans[1].append(temp)
        temp = []

for i, next_i in zip(lst, lst[1:]):
    if i > next_i and i - next_i == 1:
        connect = True
        temp.append(i)
    
    if (connect and next_i == 1) or next_i == 1:
        count += 1
        connect = False
        temp.append(next_i)
        ans[1].append(temp)
        temp = []

        
ans[0] = count
print(ans)