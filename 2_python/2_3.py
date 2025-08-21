def mod_position(arr, s):
    arr = list(arr)
    ans = []
    for i in range(len(arr)):
        if not((i+1) % s):
            ans.append(arr[i])
    return ans
print("*** Mod Position ***")
msg, i = input("Enter Input : ").split(",")
print(mod_position(msg, int(i)))