#Create a function factorial(x) that takes an integer and returns the product of all the positive integers less than or equal to n.
def factorial(n):
    product=1
    while(n!=1):
        product*=n
        n=n-1
    print(product)
a=int(input("enter the number: "))
factorial(a)
