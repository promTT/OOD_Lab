def binarySearch(arr, x):
    low = 0
    high = len(arr) - 1

    if x < arr[0]:
        return -1

    if x > arr[-1]:
        return 999

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return float(mid)
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    if 0 <= high < len(arr)-1 and arr[high] < x < arr[low]:
        frac = (x - arr[high]) / (arr[low] - arr[high])
        return high + frac
    
    return float(-1)


def findPercentile(i, n):
    if i == 999:
        return 100
    ans = (i + 1) * 100 / n
    return ans if ans != 100 and ans != 0 else int(ans)
arr, target = input("Enter Input : ").split("/")
arr = [float(i) for i in arr.split()]
target = float(target)
index = binarySearch(arr, target)

print(f"\nindex      :   {index}")
print(f"percentile :   {findPercentile(index, len(arr))}")