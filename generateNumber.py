#Create a function generateNumbers(num) that takes in a positive number as argument and returns a list of number from 0 to that number inclusive. Note: The function range(5) will return a list of number [0, 1, 2, 3, 4].
def generateNumber(num): 
    list1=[]
    for i in range(0,num+1):
        list1.append(i)
    print(list1)
n=int(input("enter the no.: "))
generateNumber(n)
