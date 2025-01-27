def isPrime(n):
    if n < 2:
        return False
    factors = []
    for i in range(n):
        if n % (i+1) == 0:
            factors.append(i)
    return (len(factors) == 2)


n = 1
j = []
while len(j) < 100:
    if isPrime(n):
        j.append(n)
    n+=1

print(j)

