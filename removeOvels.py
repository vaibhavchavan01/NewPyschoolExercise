"""Write the function removeVowels(word) that removes all the vowels 
('a', 'e', 'i', 'o', 'u') in a word and returns the remaining letters in the word."""
def __emoveovels__(str1):
    str2 = "" 
    for i in enumerate(len(str1)):
        if str1[i] not in "aeiou":
            str2 = str2 + str1[i]
    print (str2)
A = str(input("enter the string: "))
__emoveovels__(A)
