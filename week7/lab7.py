'''
Given a dictionary of keys that are stringd and or integersm 
values are lists, write snipper of code that returns thhe total exemments of 
all elements that have keys as stri
d = {3: [3,6] 'a}: [3,4,50], b: [4,5,6,7]}


'''

'''
write a function wordTally that takes an interger element n and reads n words from the user, reader may eneter same word
function should tall up how many times each word occurs 

may only create one dictionary
'''

def no(dict):
    count = 0 
    for key in dict:
        if type(key) == str:
            count += len(dict[key])
    return count

d = {3: [3,6], 'a': [3,4,50], 'b': [4,5,6,7]}

print(no(d))


def wordTally():
    dict = {}
    n = int(input())
    for _ in range(n):
        word = input()
        if word in dict:
            dict[word] = dict.get(word) + 1
        else:
            dict[word] = dict.get(word, 1)
    return dict


        

'''
inverse a dictionary 
'''

def inverse(d):
    new_d = {}
    for key in d:
        new_d[d[key]] = key
    
    return new_d

print(inverse({3: 5, 4: 6, 7:9}))