#Create a function addNumbers(x) that takes a number as an argument and adds all the integers between 1 and the number (inclusive) and returns the total number.
def addNumbers(n):
    sum=0
    i=0
    while(i!=n):
        sum+=i
        i+=1
    print(sum)
a=int(input("enter the number: "))
addNumbers(a)
