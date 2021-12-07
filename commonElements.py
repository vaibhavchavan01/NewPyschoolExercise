def common_elements(tupels1,tuples2):
    list1=[]
    for i in tupels1:
        if i not in tuples2:
            list1.append(i)
    return tuple(list1)
    

a=(1,2,3,'a','b')
b=(1,2,'a')
print(common_elements(a,b))    