def filter1():
    a=[5, -2, 8, 1, -1]
    s=filter(lambda x:x>0,a)
    print(list(s))
filter1()