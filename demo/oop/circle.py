class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f"Point({self.x}, {self.y}) and radius {self.r}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.r == other.r

    def __lt__(self, other):
        #print('__gt__')
        return self.r < other.r


c1 = Circle(10, 20, 15)
c2 = Circle(10, 20, 15)
c3 = Circle(1, 1, 20)

print(c1)  # str(c1) --> c1.__str__()
print(c1 == c2)  # c1.__eq__(c2)
print(c1 == c3)  # c1.__eq__(c3)
# print(c1 > c3)  # c1.__gt__(c3)

l = [Circle(1, 2, 10), Circle(2, 20, 15), Circle(10, 20, 5)]
for c in sorted(l):
    print(c)
