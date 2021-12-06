#code no-11
def create_stars(n):
    if n==1:
        print("*")
        return n
    else:
        print("*",end="")
        return create_stars(n-1)
n=int(input("enter the number: "))
n=(2**n)
create_stars(n)
