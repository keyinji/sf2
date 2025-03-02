def combine(d1, d2):
    '''
    a new dict where each key is a jet that is both in d1 and d2
    the value associated with each key is the new dict is the sum of sll the in
    integers on one in this lsy 
    '''
    new_dict={}
    for key in d1:
        if key in d2:
            new_dict[key] = sum(d1[key]) + sum(d2[key])
    return new_dict
  


d1 = {1: [2], 4: [5,6]}
d2 = {4: [8]}

print(combine(d1, d2))