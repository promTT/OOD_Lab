def reverseSort(lst):
    if len(lst) == 0:
        return []
    m = max(lst)
    lst.remove(m)
    return [] + [m] + reverseSort(lst)

inp = input("Enter your List : ").split(",")
inp = [int(i) for i in inp]
print(f"List after Sorted : {reverseSort(inp)}")