from __future__ import annotations
from functools import total_ordering

@total_ordering
class Account:
    def __init__(self, gold):
        self.gold = gold
    def addGold(self, amount: int) -> None:
        '''add gold to this account''' 
        self.gold += amount
    def zeroGold(self):
        self.gold = 0

    def doubleGold(self) -> None:
        self.gold *= 2
    
    def __lt__(self, other: Account) -> bool:
        return isinstance(other, Account) and self.gold < other.gold 
    
    def __eq__(self, other: Account) -> bool:
        return isinstance(other, Account) and self.gold == other.gold 
    

a1 = Account(500)
print(a1)
a2 = Account(500)
a3 = Account(56)
a4 = Account(34)



print(a1 == a2)
print(a4 < a3)

print(a4 > a1)
print(a1 != a2)