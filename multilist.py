def multilist(num):
    list1=[1,2,3,4,5]
    list2=[]
    for i in range(0,num):
        list2.append(set(list1))
    print(list2)
multilist(5)