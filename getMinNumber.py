#minimum number of the list
def getMinNumber(numbers): 
    min=list1[0]
    for i in range(0,len(list1)):
        if(min>list1[i]):
            min=list1[i]
    print(min)
list1=[3,2,1,2,3]
getMinNumber(list1)