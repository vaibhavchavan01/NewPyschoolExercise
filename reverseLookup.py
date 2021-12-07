def reverse_lookup(NEW_DICT, POSITION):
    '''Write a function reverseLookup(dictionary, value) that takes in a dictionary 
       and a value as arguments and returns a sorted list of all keys that contains the value. 
       The function will return an empty list if no match is found.'''
    list1 = []
    for key,val in NEW_DICT.items():
        if val ==  POSITION:
            list1.append(key)
    print(sorted(list1))

NEW_DICT = {'a':1, 'b':2, 'c':2, 'd':3, 'e':4, 'f':5}
POSITION = int(input("enter the element: "))
reverse_lookup(NEW_DICT, POSITION)      