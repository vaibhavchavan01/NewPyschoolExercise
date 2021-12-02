#Create a function generateNumbers(start, end) that takes in two numbers as arguments and returns a list of numbers starting from start to the end number (inclusive) specified in the arguments. 
#Note: The function range(x, y) can takes in 2 arguments. 
#For example, range(1, 5) will return a list of numbers [1,2,3,4].
def generateNumber(start, end): 
    list1=[]
    for i in range(start,end):
        list1.append(i)
    print(list1)
a=int(input("enter the start value: "))
b=int(input("enter the end value: "))
generateNumber(a,b)