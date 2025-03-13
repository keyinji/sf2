def read_birthdays():
    birthdays = {}
    while True:
        line = input("month day name: ")
        if line == 'stop':
            return birthdays
        month, day, name = line.split()
        if month not in birthdays:
            birthdays[month] = {day: [name]}
        elif day not in birthdays[month]:
            birthdays[month][day] = [name]
        else:
            birthdays[month][day].append(name)



def mostCovered(birthdays):
    new_d = {}
    for key in birthdays:
        sum = 0
        for k in birthdays[key]:
            new_d[key] = sum + len(birthdays[key][k])
    return max(new_d, key = new_d.get)
        

print(mostCovered({'f': {'23': ['ok', 'ok']}, 'p': {'20': ['19']}, 'j': {'10': ['23']}}))

def invert(birthdays):
    inverted_birthdays = {}
    for month, days in birthdays.items():
        for day, names in days.items():
            for name in names:
                inverted_birthdays[name] = (month, day)
    return inverted_birthdays

print(invert({'f': {'23': ['k', 'ok']}, 'p': {'20': ['19']}, 'j': {'10': ['23']}}))

    
