class Laptop:
    def __init__(self, weight, color):
        self.weight = weight
        self.color = color
    def display(self):
        print(self.weight, self.color)
            
laptop = Laptop(1.2, "Silver") #Create a Laptop object
laptop.display()