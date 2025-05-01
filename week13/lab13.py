class EvenIterator:
    def __init__(self, start, end):
        self.current = start if start % 2 == 0 else start + 1
        self.end = end

    def __iter__(self):
        return self


    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        even_number = self.current
        self.current += 2
        return even_number

even = EvenIterator(2, 10)
for num in even:
    print(num)

class Fibonacci:
    def __init__(self, n):
        self.n = n  
        self.current_term = 0
        self.first = 0
        self.second = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_term >= self.n:
            raise StopIteration
        if self.current_term == 0: 
            self.current_term += 1
            return self.first
        elif self.current_term == 1:  
            self.current_term += 1
            return self.second
        next_value = self.first + self.second
        self.first, self.second = self.second, next_value
        self.current_term += 1
        return next_value

# Example usage
# fib = Fibonacci(8)
# for num in fib:
#     print(num)

def recMin(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        min_val = recMin(lst[1:])
        if lst[0] < min_val:
            return lst[0]
        else:
            return min_val

def recInt(st):
    if len(st) == 1:  
        return int(st)
    return int(st[0]) * (10 ** (len(st) - 1)) + recInt(st[1:])  

def recPal(st):
    if len(st) <= 1:  
        return True
    if st[0] != st[-1]:  
        return False
    return recPal(st[1:-1])  

def recVo(st):
    if not st:
        return 0
    if st[0].lower() in "aeiou":  
        return 1 + recVo(st[1:])  
    return recVo(st[1:])  

def hasMoreVowels(st, vowels=0, consonants=0):
    if not st:  
        return vowels > consonants  
    if st[0].lower() in "aeiou": 
        return hasMoreVowels(st[1:], vowels + 1, consonants)
    elif st[0].isalpha():
        return hasMoreVowels(st[1:], vowels, consonants + 1)
    return hasMoreVowels(st[1:], vowels, consonants)  



class EvenFilter:
    def __init__(self, iterable):
        self.__iterable = iterable
    
    def __iter__(self):
        return self
    
    def __next__(self):
        for item in self.__iterable:
            if item % 2 == 0:
                return item
        raise StopIteration

for num in EvenFilter(range(1,21)):
    print(num)