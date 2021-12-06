def sumNumbersFromOne(x):
    if x < 1:
        return "Invalid"
    if x == 1:
        return x
    else:
        
        return x + sumNumbersFromOne(x-1) 
n1 = int(input("enter the number: "))

print(sumNumbersFromOne(n1))