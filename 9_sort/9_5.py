def generate_combinations(lst, current=None):
    if current is None:
        current = []
    if not lst:
        return [current] if current else []

    result = []
    result += generate_combinations(lst[1:], current + [lst[0]])
    result += generate_combinations(lst[1:], current)
    return result


def select_sum_subsets(subsets, target):
    result = []
    for subset in subsets:
        if sum(subset) == target:
            result.append(sort_numbers(subset))
    return result


def sort_numbers(lst):
    for j in range(len(lst) - 1, 0, -1):
        for i in range(j):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


def sort_subsets(subsets):
    for j in range(len(subsets) - 1, 0, -1):
        for i in range(j):
            if len(subsets[i]) > len(subsets[i + 1]) or \
               (len(subsets[i]) == len(subsets[i + 1]) and subsets[i] > subsets[i + 1]):
                subsets[i], subsets[i + 1] = subsets[i + 1], subsets[i]
    return subsets


# --- main ---
target_sum, numbers = input("Enter Input : ").split("/")
target_sum = int(target_sum)
numbers = [int(x) for x in numbers.split()]

all_subsets = generate_combinations(numbers)
valid_subsets = select_sum_subsets(all_subsets, target_sum)
sorted_subsets = sort_subsets(valid_subsets)

if not sorted_subsets:
    print("No Subset")
else:
    for subset in sorted_subsets:
        print(subset)