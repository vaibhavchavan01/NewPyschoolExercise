#Create a function genSet() that takes in a list of numbers and returns a sorted set.
def gen_set(n):
    list1=[]
    temp=0
    for i in range(n):
        num=int(input())
        list1.append(num)
    list1=set(list1)
    list1=list(list1)
    print(list1)
    for i in range(0,len(list1)):
        for j in range(0,len(list1)):
            if(list1[i]<list1[j]):
                temp=list1[i]
                list1[i]=list1[j]
                list1[j]=temp
    print(list1)
    #for i in range(n):
a=int(input("enter the number: "))
gen_set(a)