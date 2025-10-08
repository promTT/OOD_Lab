def recursive_sort_and_swap(arr, n):
    if n <= 1:
        return

    max_index = 0
    for i in range(1, n):
        if arr[i] > arr[max_index]:
            max_index = i

    if max_index != n - 1:
        arr[max_index], arr[n - 1] = arr[n - 1], arr[max_index]
        print(f"swap {arr[max_index]} <-> {arr[n-1]} : {arr}")

    recursive_sort_and_swap(arr, n - 1)

input_str = input("Enter Input : ")
my_list = [int(x) for x in input_str.split()]

recursive_sort_and_swap(my_list, len(my_list))

print(my_list)