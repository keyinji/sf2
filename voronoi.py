villages = int(input("How many villages are there: "))

num = []


for i in range(villages):
    number  = input(f"Whats the name of your {i} village: ")
    num.append(int(number))

num.sort()
print(num)

neighbor = []
for i in range(len(num)-1):
    neighborhood = (int(num[i]) + int(num[i+1])) /2
    neighbor.append(neighborhood)

print(neighbor)

hi = []
for i in range(len(neighbor)-1):
    neighbourhood = (int(neighbor[i+1]) - int(neighbor[i]))
    hi.append(neighbourhood)

print(hi)
