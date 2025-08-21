arr = input("Enter Your List : ").split()
arr = [int(i) for i in arr]
if len(arr) < 3:
    print("Array Input Length Must More Than 2")
else:
    ans = []
    arr.sort()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k] == 5:
                    if [arr[i],arr[j],arr[k]] not in ans:
                        ans.append([arr[i],arr[j],arr[k]])

    print(ans)