class Point:
    '''A class implementation of a %d-dimensional point.
        aasd
    '''
    def __init__(self, *args):
        print(args)
    def __str__(self):
        
        print(self.args)
        
point=Point(10, 20)
print(point.__doc__)


