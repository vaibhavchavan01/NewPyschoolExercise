#Create a function addNumbers(start, end) that adds all the integers between the start and end value (inclusive) and returns the total sum.
def addNumbers(start,end):
    sum=0
    while(start!=end):
        sum+=start
        start+=1
    print(sum)
a=int(input("enter the number start: "))
b=int(input("enter the number end: "))
addNumbers(a,b)
