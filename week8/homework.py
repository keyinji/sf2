'''
Frigus is behind on several assignments
He has N items.
He has M upcoming assignments
the i-th of which requires Ti items to complete 
How many assignments can FIrgus complete 


Input: 
FIrst line conmtains two interfers N and M separared by a space
Nest N lines n items M assignments 

sample input 
3 4
chalk
chesse
charger
1 
cheese
2 
coins
cash
3
charger 
chalk 
caffeine
3
cheese
charger 
chalk

'''

n, m = input().split()
n = int(n)
m = int(m)

items = set()
for _ in range(n):
    item = input()
    items.add(item)
lst = []
for i in range(m):
    no = int(input())
    set_of_words = set()
    for _ in range(no):
        word = input()
        set_of_words.add(word)
    if set_of_words.issubset(items):
        lst.append(i+1)
        

print(lst)
  
