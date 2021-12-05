# Write a function isInAlphabeticalOrder(word) that takes in a 
# word as argument and returns True if the word contains letters that are arranged in alphabetical order. 
# For example, the letter 'c' should not appear before the letter 'a'.
def isInAlphabeticalOrder(word):
	flag=0
	for i in range(0,len(word)-1):
		if word[i]<=word[i+1]:
			continue
		else:
			flag=1
			break
	if flag==1:
		return False
	else:
		return True
word=input("Enter the word to check is alphabetical order or not : ")
print(isInAlphabeticalOrder(word))