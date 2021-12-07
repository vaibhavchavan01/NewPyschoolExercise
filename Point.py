class Point:
    '''"A class implementation of 2-Dimensional point."
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # def __str__(self):
    #     return '(%d, %d)' % (self.x, self.y)

    def __add__(self, other):
        return self.x + other.x, self.y + other.y
    def __sub__(self, other):
        return self.x - other.x, self.y +  other.y
a = Point(1, 3)
b = Point(7, 2)
# c = (a+b)
print(a+b)
print(a-b)
print(a.__doc__)