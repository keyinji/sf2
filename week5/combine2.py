def combine2(d1, d2):
    for outer_key in d1:
        if outer_key in d2:  
            for inner_key in d1[outer_key]:
                if inner_key in d2[outer_key]:
                    d1[outer_key][inner_key] = sum(d1[outer_key][inner_key]) + sum(d2[outer_key][inner_key])
    return d1


d1 = {'a': {3: [2], 4: [5,6]}, "b": {7: [2,7,9]}}
d2 = {'a': {3: [8,12]}, "b": {7:[7,33]}}

{3:22}


print(combine2(d1,d2))

