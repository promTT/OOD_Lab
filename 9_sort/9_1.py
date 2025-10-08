def bubble(lst, i=0):
    if i == len(lst) - 1:
        return lst
    if lst[i] > lst[i+1]:
        lst[i], lst[i+1] = lst[i+1], lst[i]
    return bubble(lst, i+1)

def sort(lst, n=None):
    if n is None:
        n = len(lst)
    if n == 1:
        return lst
    bubble(lst)
    return sort(lst, n-1)

x = list(map(int, input("Enter Input : ").split()))
print(sort(x))