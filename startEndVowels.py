#Write the function startEndVowels(word) that returns True if the word starts and ends with vowels.
def startEndVowels(str):
    if (str[0] and str[len(str)-1]) in "aeiou":
        print("True")
    else:
        print("False")
a=str(input("enter the string: "))
startEndVowels(a) 
