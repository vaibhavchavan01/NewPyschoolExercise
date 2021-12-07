def shift_by_two(NEW_TUPLES):
    list1=list(NEW_TUPLES)
    for i in range(2):
        a=list1.pop()
        list1.insert(0,a)
    print(tuple(list1))
NEW_TUPLES=(1,2,3,4,5)
shift_by_two(NEW_TUPLES)
    