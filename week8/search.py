import time



def search(collection, target):
    '''
    search collection for target
    '''
    print('searching....')
    for i in collection:
        found = target in collection
    return found

lst = list(range(1,50000))
s = set(range(1, 50000))

start = time.time()

search(lst, 50000)

end = time.time()
print({end-start})


start = time.time()
search(s, 50000)
end = time.time()
print({end-start})




