def can_pack(max_weight, k, weights):
    box_count = 1
    current_weight = 0
    
    for w in weights:
        if w > max_weight:
            return False
            
        if current_weight + w <= max_weight:
            current_weight += w
        else:
            box_count += 1
            current_weight = w
            
    return box_count <= k


def find_minimum_weight(weights, k):
    if not weights:
        return 0

    low = max(weights)
    high = sum(weights)                   
    
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        
        if can_pack(mid, k, weights):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans



w, k = input("Enter Input : ").split("/")

wLst = [int(w) for w in w.split()]

minimum_weight = find_minimum_weight(wLst, int(k))

# Print the required output format
print(f"Minimum weigth for {k} box(es) = {minimum_weight}")