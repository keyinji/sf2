from __future__ import annotations

class Fraction:
    def __init__(self, num=0, denom=1):
        if denom == 0:
            raise ZeroDivisionError('Denominator cannot be zero')
        
        if denom < 0:
            num = -num
            denom = -denom
            
        self.num = num
        self.denom = denom
        
        # Reduce fraction to lowest terms
        if self.num != 0:
            # Find GCD using Euclidean algorithm
            a, b = abs(int(self.num)), abs(int(self.denom))
            while b:
                a, b = b, a % b
            gcd = a
            
            # Apply reduction if GCD > 1
            if gcd > 1:
                self.num = int(self.num / gcd)
                self.denom = int(self.denom / gcd)
        else:
            # If numerator is 0, set denominator to 1
            self.denom = 1

    def __repr__(self):
        if self.denom == 1:
            return f"{int(self.num)}"
        return f"{int(self.num)}/{int(self.denom)}"
    
    def __add__(self, other_fraction: Fraction) -> Fraction:
        new_num = self.num * other_fraction.denom + other_fraction.num * self.denom
        new_denom = self.denom * other_fraction.denom
        return Fraction(int(new_num), int(new_denom))
    
    def __sub__(self, other_fraction: Fraction) -> Fraction:
        new_num = self.num * other_fraction.denom - other_fraction.num * self.denom
        new_denom = self.denom * other_fraction.denom
        return Fraction(int(new_num), int(new_denom))
    
    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False
        return self.num == other.num and self.denom == other.denom
    
    def __ne__(self, other):
        return not self.__eq__(other)


# Main program
f1 = Fraction(10, 14)
f2 = Fraction(-3, -4)
print(f1)
print(Fraction(14, 20))