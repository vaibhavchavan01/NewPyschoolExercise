def power(x, y):
    if y == 0:
        return 1
    else:
        return x*power(x, y-1)
n1 = int(input("enter the number: "))
n2 = int(input("enter the number: "))

print(power(n1, n2))