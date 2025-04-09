from __future__ import annotations

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    def translate(self, dx: int, dy: int) -> None:
        '''move this point dy horizonatally and dy vertically'''
        self.x = self.x + dx
        self.y = self.y + dy
    def distance(self, other_point: Point) -> float:
        '''return distance between this point and other point'''
        a = (other_point.x - self.x) ** 2
        b = (other_point.y - self.y) ** 2
        return (a+b) ** 0.5

    def __repr__(self) -> str:
        '''return x, y coordinates as (x, y)'''
        return f'({self.x}, {self.y})'
    def __lt__(self, other_point: Point) -> bool: 
        '''return True if this point and other point are of type point a'
        and x y of this point is less than xy other point
        '''
        return isinstance(other_point, Point) and self.x < other_point.x and self.y < other_point.y
    def __eq__(self, other_point: Point) -> bool: 
        '''return True if this point and other point are of type point a'
        and x y of this point is less than xy other point
        '''
        return isinstance(other_point, Point) and self.x == other_point.x and self.y == other_point.y



p1 = Point(2, 3)
print(p1)
p1.translate(3, 7)
print(p1)
p2 = Point(5,6)

print(p1.distance(p2))


p3 = Point(0, 3)
p4 = Point(8,3)

print('p3 <? p4', p3 < p4)
print('p3 == p4', p3 == p4)