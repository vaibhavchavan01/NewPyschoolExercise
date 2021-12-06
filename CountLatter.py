'''Write the function countLetter(word, letter) that takes in a word and a letter 
as arguments and returns the number of occurrence of that letter in the word.'''

def countLetter(word, letter):
	cnt = 0
	for i in range(0,len(word)):
		if word[i]==letter:
			cnt+=1
	return cnt

print(countLetter('apple','p'))