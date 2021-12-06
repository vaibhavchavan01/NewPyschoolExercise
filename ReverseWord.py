def reverse_word(WORD1):
    for i in range(len(WORD1)):
        print(WORD1[len(WORD1)-1-i], end="")
WORD = str(input("enter the word: "))
reverse_word(WORD)