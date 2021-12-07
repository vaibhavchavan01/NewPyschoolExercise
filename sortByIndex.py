def sortByIndex(n1):
    list1=[]
    for i in range(0,n1):
        a=int(input())
        b=str(input()) 
        c=(a, b)        
        list1.append(c)
    # print(dict(list1))
    a=dict(list1)
    
    print(tuple(a.values()))

# a=int(input("enterthe number: "))
# b=tuple(input("enter the value:"))
n=int(input("enter the number: "))
sortByIndex(n)