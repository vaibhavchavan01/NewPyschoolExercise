def mirror_text(word1, word2):
    '''Write a function mirrorText(word1, word2) that takes in 2 words as arguments and 
       returns a new word in the following order: word1word2word2word1.
    '''
    print(word1+word2+word2+word1)
STRING1 = str(input("enter the word1: "))
STRING2 = str(input("enter the word2: "))
mirror_text(STRING1, STRING2)
