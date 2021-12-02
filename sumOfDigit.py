#Write a function sumOfDigit(number) that takes in a number as argument and returns the sum of the individual digit in the number.
def sumOfDigit(n):
    sum=0
    for i in range(n):
        if(n==0):
            break
        sum+=(n%10)
        n=int(n/10)
    print(sum)
a=int(input("enter the number: "))
sumOfDigit(a)
