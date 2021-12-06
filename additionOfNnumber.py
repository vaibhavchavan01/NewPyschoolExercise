#code no -09
def addition_of_number(n):
        if n==0:
            return n
        else:
            return n + addition_of_number(n-1)
n=int(input("enter the number: "))
print(addition_of_number(n))