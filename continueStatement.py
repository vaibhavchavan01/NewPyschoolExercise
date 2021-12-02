#use continue statement within the loop
def continue_statement(n):
    for i in range(0,n):
        if i==n-2:
            continue
        print(i)
a=int(input("enter the start number: "))
continue_statement(a)