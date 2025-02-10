for i in range(1, 11):
    print("*"*i)


for i in range(1, 11):
    j = 11 - i
    print("*"*j)

for i in range(1, 11):
    j = 11 - i
    print(" "*(i-1)+"*"*j)

for i in range(1, 11):
    j = 11 - i
    print(" "*(j-1)+"*"*i)