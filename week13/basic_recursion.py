def iterSum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total


def recSum(n):
    if n == 1:
        return 1
    else:
        return n + recSum(n-1)


def recFactorial(n):
    if n == 0 or n == 1:
        return 1
    return recFactorial(n-1) * n



def recFib(n):
    if n == 0 or n == 1:
        return n
    else:
        return recFib(n-1) + recFib(n-2)
    
def recFibTail(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return recFibTail(n-1, b, a+b)