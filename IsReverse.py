# Write the function isReverse(word1, word2) 
# that takes two words as arguments and 
# returns True is the second word is the reverse of the first word.
def isReverse(word1, word2):
	str = word1[::-1]
	if str==word2:
		return True
	else:
		return False
word1=input("Enter The first word : ")
word2=input("Enter The second word : ")
print(isReverse(word1,word2))