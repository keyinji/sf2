# def new(kinds, counts, sighting):
#     if sighting not in kinds:
#         kinds.append(sighting)
#         counts.append(0)
#     i = kinds.index(sighting)
#     counts[i] += 1

# kinds = ['Monarch', 'Painted Lady', "Bronze Copper", "Orange"]
# counts = [5, 2, 12, 7]

# for i in range(len(kinds)):
#     print(f'{kinds[i]}: {counts[i]}')

# new(kinds, counts, 'Monarch')


# for i in range(len(kinds)):
#     print(f'{kinds[i]}: {counts[i]}')

butterflies = {"m": 5, "j":7}

for k in butterflies:
    print(f'{k}: {butterflies[k]}')

def new_sighting(butterflies, sighting):
    butterflies[sighting] = butterflies.get(sighting) + 1


new_sighting(butterflies ,'m')

for k in butterflies:
    print(f'{k}: {butterflies[k]}')
    