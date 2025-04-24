from __future__ import annotations
from functools import total_ordering


class Empty(Exception):
    pass

@total_ordering
class Stack:
    def __init__(self):
        self.__data = []

    def __len__(self):
        return len(self.__data)

    def isEmpty(self):
        return len(self.__data) == 0

    def push(self, value):
        self.__data.append(value)
    
    def top(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.__data[-1]

    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self.__data.pop()
        
    def __repr__(self):
        import os
        import time
        os.system('')
        
        YELLOW = '\033[33m'
        WHITE = '\033[37m'
        COLORS = ['\033[31m', '\033[32m', '\033[34m', '\033[35m', '\033[36m']
        RESET = '\033[0m'
        
        if self.isEmpty():
            return f"{WHITE}Empty Stack{RESET}"
            
        colored_items = []
        current_time = int(time.time())
        
        for i, item in enumerate(self.__data):
            if i == len(self.__data) - 1:
                color = YELLOW
            else:
                color_index = (i + current_time) % len(COLORS)
                color = COLORS[color_index]
            colored_items.append(f"{color}{item}{RESET}")
            
        return ' '.join(colored_items)

    def __lt__(self, other):
        return len(self.__data) < len(other.__data)
    
    def __eq__(self, other):
        return len(self.__data) == len(other.__data)

if __name__ == '__main__':
    print("\nDemo of colored stack:")
    s = Stack()
    s.push(5)
    s.push(3)
    s.push(7)
    s.push(2)
    print("Stack after pushing 5, 3, 7, 2:")
    print(s)
    
    print("\nPopping one element:")
    s.pop()
    print(s)
    
    print("\nStack top:", s.top())
    print("Stack size:", len(s))
    print("Is stack empty?", s.isEmpty())


def is_balanced(string):
    stack = Stack()
    opening = "({["
    closing = ")}]"
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in string:
        if char in opening:
            stack.push(char)
        elif char in closing:
            if stack.isEmpty():
                return False
            top = stack.pop()
            if top != pairs[char]:
                return False
    
    return stack.isEmpty()

