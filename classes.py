# classes.py

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
p1 = Point(3,5)
p2 = Point(4,6)
print(p1.x)
print(p2.x)
print(p1.y)
print(p2.y)

slope = (p2.x - p1.x) / (p2.y - p1.y)
print(p2.x - p1.x)
print(p2.y - p1.y)
print(f"slope is {slope}")
