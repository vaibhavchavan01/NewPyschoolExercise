"""
Write the function search(word, substring) that takes in a word and a 
substring as arguments and returns the position (0 indexed) of the substring if it is 
found in the word. The function returns -1 if the substring is not found.
"""
def find_substring(new_string, substring):
    if substring not in new_string:
        return False
    else:
        return True
STRING_INPUT = str(input("Enter the string :  "))
SUBSTRING = str(input("Enter the substring: "))
print(find_substring(STRING_INPUT, SUBSTRING))