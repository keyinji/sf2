'''
There are many ways to write the e-mail adresses.
--> take a gmail adress and a + and a string before the @symbol and email is still valid.
example: 
louisa.haruyunyan@gmail.com
lou.isa.hjar.uty.yu.un.ya.n@gmail.com
upper and loswer case differences throughout the addresses are also ignored
examples:
LousISA.Hautyunyan@gmail.com
Given emai addresses, dtermine the num of them that are unique.
the rueles for e-mail adresses are the sa,e as above
--> chatacyers from + sumbol to the @ symbol are ignored
--> dots are ignored
--> case throughout the entire address is ignored

input specification :
--> first line of inpu t is int n :
designating number of e-mail addresses to read
--? the next n lines are the n addresses
-->atleast 1 character before @ symbol
characters before @ symbol can be letters , 
plus, numbers, dots
after @, you can have all except plus.'''


def clean(address):
    # remove everything between + and @ symbols
    plus_index = address.find('+')
    if plus_index != -1:
        at_index = address.find('@')
        address = address[:plus_index] + address[at_index:]
    # remove all dots
    address = address.replace(".", '')
    # make everything lowercase.
    address = address.lower()
    return address


# To do
# read the input
n = int(input('num of email addresses?'))
addresses = []
for i in range(n):
    address = input(f'email address {i}?')
    address = clean(address)
    
    if address not in addresses:
        addresses.append(address)
