# Write a function echoWord(word) that takes in a word as arguments and 
# returns a word that repeats itself based on the number of letter in the word.
def echoWord(word):
	return word*len(word)
word=input("Enter The Word : ")
print(echoWord(word))