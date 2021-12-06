# Write the function startWithVowel(word) that takes in a 
# word as argument and returns a substring that starts with the first vowel found in the word. 
# The function returns 'No vowel' if the word does not contain vowel.
def startWithVowel(word):
	flag=cnt=0
	l=['a','e','i','o','u','A','E','I','O','U']
	if word[0] in l:
		return word
	else:
		for i in range(0,len(word)):
			cnt+=1
			if word[i] in l:
				flag=1
				break
	if flag==1:
		return word[cnt-1:]
	else:
		return "No vowel"
word=input("Enter word : ")
print(startWithVowel(word))