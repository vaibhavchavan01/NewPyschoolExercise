def add_update_dictionary(DICTIONARY):
    '''add element in dictionary'''
    DICTIONARY['id']=1
    print(DICTIONARY)
    if DICTIONARY['age']==25:
        DICTIONARY['age']=125
        print("updated Dictionary-",DICTIONARY)
DICT_KET_VALUE = {'name':'john', 'age':25, 'Company':'Amazatic'}
add_update_dictionary(DICT_KET_VALUE)
DICT_KET_VALUE.items