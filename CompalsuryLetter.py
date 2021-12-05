# Write a function isAllLettersUsed(word, required) that takes in a word as the first argument and 
# returns True if the word contains all the letters found in the second argument.
def isAllLettersUsed(word, required):
	flag=0
	for i in required:
		if i not in word:
			flag=1
			break
	if flag==1:
		return False
	else:
		return True
word1=input("Enter The first word : ")
word2=input("Enter The sequence to check in word : ")
print(isAllLettersUsed(word1,word2))