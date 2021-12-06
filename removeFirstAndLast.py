def removeFirstAndLast(list1):
    count=0
    list2=[]
    for i in range(1,len(list1),3):
        if(i%2!=0):
            list2.append(i)
    list2.remove(list2[0])
    list2.remove(list2[-1])
    print(list2)
list1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
removeFirstAndLast(list1)
