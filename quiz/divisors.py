lst = []
lst2 = []

def divisors(n):
    n = abs(n)
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
            lst.append(i*-1)
    print(lst)

divisors(-10)