#Create a function addNumbers(start, end) that takes in two positive numbers as arguments and 
#returns the sum of all the number between the start and end number (inclusive).
def addNumber(start,end):
    sum=0
    for i in range(start,end+1):
        sum+=i
    print(sum)
a=int(input("enter the start number: "))
b=int(input("enter the end number: "))
addNumber(a,b)
