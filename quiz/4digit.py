n = int(input("Please enter a 4 digit number: "))

n += 1 

n = str(n)


while True:
    if n[0] == n[1] or n[0] == n[2] or n[0] == n[3] or n[1] == n[2] or n[1] == n[3] or n[2] == n[3]:
        n = int(n)
        n += 1 
        n = str(n)
    else:
        break

print(n)


def isDistinct(year) -> bool:
    s = str(year)
    digits_used = []
    for char in s:
        if char in digits_used:
            return False
        digits_used.append(char)
    return True

year = int(input())
year += 1


while not isDistinct(year):
    year += 1



num = 1002
while len(set(list(str(num)))) != 4:
    num += 1
print(num)