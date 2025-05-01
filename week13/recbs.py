def binary_search(lst, low, high, target):
    if low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            return binary_search(lst, mid + 1, high, target)
        else:
            return binary_search(lst, low, mid - 1, target)
    else:
        return -1