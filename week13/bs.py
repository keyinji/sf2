def bs(lst, n):
    low = 0
    high = len(lst) - 1
    mid = 0
    while low <= high:
        mid = (low+ high) // 2

        if lst[mid] < n: #target in right half
            low = mid + 1
            print("HI")
        elif lst[mid] > n:
            high = mid - 1
            print("OK")
        else:
            return mid
    return False 

print(bs([1,2,3,4,5,6,7,8,9], 4))
        