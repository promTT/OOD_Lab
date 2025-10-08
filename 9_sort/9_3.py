def quick_sort(items, key_func=lambda x: x[1]):
    """Sort list in-place using quicksort."""
    def _sort(lst, start, end):
        if start < end:
            pivot_index = _partition(lst, start, end)
            _sort(lst, start, pivot_index - 1)
            _sort(lst, pivot_index + 1, end)

    def _partition(lst, start, end):
        if start == end - 1:  # two elements only
            if key_func(lst[start]) > key_func(lst[end]):
                lst[start], lst[end] = lst[end], lst[start]
            return start

        pivot = lst[start]
        left, right = start + 1, end

        while left < right:
            while left < end and key_func(lst[left]) <= key_func(pivot):
                left += 1
            while right > start and key_func(lst[right]) >= key_func(pivot):
                right -= 1
            if left < right:
                lst[left], lst[right] = lst[right], lst[left]

        lst[start], lst[right] = lst[right], lst[start]
        return right

    _sort(items, 0, len(items) - 1)


def sort_and_display(data):
    print("----------------------------------------")
    print("Sort by price :")
    tmp = data[:]
    quick_sort(tmp, key_func=lambda x: x[1])
    print_items(tmp)

    print("----------------------------------------")
    print("Sort by price and alphabet :")
    tmp = data[:]
    quick_sort(tmp, key_func=lambda x: (x[1], x[0]))
    print_items(tmp)


def print_items(data):
    for i, (name, price) in enumerate(data):
        print(f"{i+1:>2}. {name:<12}{price:>4}")


# --- Main program ---
inp = input("Enter Input : ").split(",")
data = [(name.strip(), int(price)) for item in inp for name, price in [item.split()]]
sort_and_display(data)