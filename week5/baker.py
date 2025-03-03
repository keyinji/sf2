franchises, days = input().split()

donuts = []

for i in range(int(days)):
    donut = input().split()
    donuts.append(donut)
    
donuts = [[int(x) for x in sublist] for sublist in donuts]
transposed_donuts = [[donuts[i][j] for i in range(len(donuts))] for j in range(len(donuts[0]))]

sum_donuts = [sum(sublist) for sublist in donuts]
sum_transposed_donuts = [sum(sublist) for sublist in transposed_donuts]

total_sum = sum_donuts+ sum_transposed_donuts

count = 0
for i in total_sum:
    if i % 13 == 0:
        count += (i//13)
        
print(count)

