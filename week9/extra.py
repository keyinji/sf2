'''
consider states and cities in thew i
. each state is given a two letter ab
you are taskeds to read n cities and states frtom user and determine the number of spercial pairs 
here is example of special pair
SCRANTON PA and PARKER SC: 
this is special since SC PA and PA SC
task is to dertermine the number of special pairs of cities in the provided input

first line is n, th number of citites 
next n lines one per city
l;ine give name of city in uppercase a spcae and its abbreviation

output number of special pairs of cities
12
SCRANTON PA
MANISTEE MI
NASHUA NH
PARKER SC
LAFAYE CO
WAS WA
MIDD MA
MADISOn MI
MIL MA
MIDDLE MA
COVI LA
LAKE CO

9


'''
n = int(input())
city_state_pairs = []
for _ in range(n):
    city_state_pairs.append(input().split())

special_pair_count = 0

for i in range(n):
    for j in range(i + 1, n):
        city1, state1 = city_state_pairs[i]
        city2, state2 = city_state_pairs[j]
        
        
        if state1 == city2[:2] and state2 == city1[:2]:
            special_pair_count += 1

print(special_pair_count)
