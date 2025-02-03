lst = []
lst2 = []

def divisors(n):
    n = abs(n)
    for i in range(1, n+1):
        if n % i == 0:
            lst.append(i)
    for j in lst:
        lst2.append(j*-1)
    print(lst + lst2)

divisors(-10)