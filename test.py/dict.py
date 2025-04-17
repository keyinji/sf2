def d(n):
    count = 0
    for key in n:
        if type(key) == str:
            count += len(n[key])
    return count

def word():
    n = int(input())
    d = {}
    for i in range(n):
        word = input()
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    print(d)


def invert(n):
    new_dict = {}
    for key in n:
        if n[key] in new_dict:
            new_dict[n[key]].append(key)
        else:
            new_dict[n[key]] = [key]
            
    return new_dict
    
def word(n, k):
    new_dict = {}
    for i in range(len(n)):
        if n[i] in new_dict:
            new_dict[n[i]] = new_dict[n[i]] + 1
        else:
            new_dict[n[i]] = 1

    
word(["hi", "hi", "h"], 1)
    
    
    