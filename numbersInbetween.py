#code no -10
def numbers_in_between(n1, n2):
    if n2<1:
        print("Invalid")
        return n1
    if n1==n2:
        print(n1)
        return n1
    else:
        print(n1, end=",")
        return numbers_in_between(n1+1,  n2)
n1 = int(input("enter the start number: "))
n2 = int(input("enter the  last number: "))
numbers_in_between(n1, n2)