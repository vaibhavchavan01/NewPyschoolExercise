'''A string contains a sequence of characters. 
Elements within a string can be accessed using index that starts from 0. 
Write the function getChar(word, pos) that takes in a word and 
a number as argument and returns the character at that position.'''
def getChar(word, pos):
	if len(word)>pos:
		return word[pos]
	else:
		return "Invalid Range."
word=input("Enter The word : ")
pos=int(input("Enter The position to get character : "))
print(pos," position element is = ",getChar(word,pos))