#Create a function addEvenNumbers(start, end) that takes in two positive numbers as arguments 
#and returns the sum of all the even numbers between the start and end number (inclusive).
def addEvenNumbers(start,end):
    sum=0
    for i in range(start,end+1):
        if i%2==0:
            sum+=i
    print(sum)
a=int(input("enter the start number: "))
b=int(input("enter the end number: "))
addEvenNumbers(a,b)