out = open('accounts.txt', 'w')

for i in range(5):
    ok = input()
    out.write(ok + '\n')

out.close()



'''
from accounts.txt read each line and create disctionary of dicstionanrues
outer dictionary is the accountn umber
inner dict key is lant name and value is balance print created dict

'''