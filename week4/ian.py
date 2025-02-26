lst1 = input("Input 1: ").split()

for i in range(len(lst1)):
    lst1[i] = int(lst1[i])

n = lst1[0]
m = lst1[1]
d = lst1[2]

laundry = 0

if m > 1:
    lst2 = input("Input 2: ").split()

    for i in range(len(lst2)):
        lst2[i] = int(lst2[i])
else:
    lst2 = []
    
total = n


for i in range(1, d+1):
    if n == 0:
        laundry += 1
        n = total  
    if i in lst2:
        total += 1
        n += 1
    n -= 1

print(laundry)



