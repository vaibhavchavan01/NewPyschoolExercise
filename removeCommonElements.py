def removeCommonElements(t1, t2):
    t3=[]
    if t1>=t2:
        for i in t1:
            if i not in t2:
                t3.append(i)
        print(tuple(t3))

t1=('b','a','c','d')
t2=('a','b','c')
removeCommonElements(t1, t2)