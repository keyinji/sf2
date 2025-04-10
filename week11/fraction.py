from __future__ import annotations

class Fraction:
    def __init__(self, num = 0, denom = 1):
        self.num = num
        self.denom = denom
        if denom == 0:
            raise ZeroDivisionError('Denominator cannot be zero')
        if denom < 0 and num > 0:
            self.denom = -denom
            self.num = -num
        elif denom < 0 and num < 0:
            self.denom = -denom
            self.num = -num

        value = 1
        list1 = [x for x in range(1, self.num+1) if self.num%x == 0]
        list2 = [x for x in range(1, self.denom+1) if self.denom % x == 0]
        list1 = list1[::-1]
        for i in list1:
            value = i
            if i in list2:
                break
        self.num = self.num / value
        self.denom = self.denom/value

    def __repr__(self):
        return f"{self.num}/{self.denom}"
    
    
    def __add__(self, other_fraction: Fraction)-> Fraction:    

        self.num *= other_fraction.denom
        other_fraction.num *= self.denom
        self.num += other_fraction.num
        
        self.denom *= other_fraction.denom
        return Fraction(int(self.num), int(self.denom))
    def __sub__(self, other_fraction: Fraction)-> Fraction:    

        self.num *= other_fraction.denom
        other_fraction.num *= self.denom
        self.num -= other_fraction.num
        
        self.denom *= other_fraction.denom
        return Fraction(int(self.num), int(self.denom))
    
    def __eq__(self, other_fraction: Fraction):
        return self == other_fraction and isinstance(other_fraction, Fraction)
    def __ne__(self, other_fraction: Fraction):
        return self == other_fraction and isinstance(other_fraction, Fraction)



# Main program
f1 = Fraction(5,7)
f2 = Fraction(-3,-4)
print(f1 == f2)
print(Fraction(14,20))