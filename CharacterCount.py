def character_count(NEW_INPUT):
    INITIAL_DICTIONARY = {}
    for i in USER_INPUT:
        if i in INITIAL_DICTIONARY:
            INITIAL_DICTIONARY[i] += 1
        else:
            INITIAL_DICTIONARY[i] = 1
    print(INITIAL_DICTIONARY)



USER_INPUT = str(input("enter the string: "))
character_count(USER_INPUT)