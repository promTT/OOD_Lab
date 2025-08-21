def fibo(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fibo(n-1) + fibo(n-2)

def getW(purify, weight):
    if purify == 1:
        return weight

    ab = 2 * weight + 1 - fibo(purify - 1)

    if ab < 2:
        return -1
    
    if ab % 2 == 0:
        a = b = ab // 2
    else:
        a = ab // 2
        b = ab - a

    wa = getW(purify - 1, a)
    wb = getW(purify - 1, b)
    
    return wa + wb

n,w= input("Purity and Weight needed: ").split()
result = getW(int(n), int(w))
print(f"Total weight of used minerals with Purity 1 : {result}")