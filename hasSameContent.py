def has_same_content(HAS_TUPLES):
    if sum(HAS_TUPLES[0])==sum(HAS_TUPLES[1]):
        return True
    else:
        return False
HAS_TUPLES=(1,2),(2,1)
print(has_same_content(HAS_TUPLES))
