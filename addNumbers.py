#Create a function addNumbers(num) that takes in a positive number as argument and returns the 
# sum of all the number between 0 and that number (inclusive).
def addNumber(num):
    sum=0
    for i in range(0,num+1):
        sum+=i
    print(sum)
n=int(input("enter the no.: "))
if(n<0):
    print("please enter the positive number")
else:
    addNumber(n)