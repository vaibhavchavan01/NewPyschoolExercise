def find_duplicate(NEW_DICT):
    NEW_DICT1={}
    for key, val in NEW_DICT.items():
        if val not in NEW_DICT1.values():
            NEW_DICT1[key] = val
    print(NEW_DICT1)
NEW_DICT = {"firstname": "Albert", "nickname": "Albert", "surname": "Likins", "username": "Angel"}
find_duplicate(NEW_DICT)