# Write the function getVowels(word) that takes in a 
# word as an argument and returns the vowels ('a', 'e', 'i', 'o', 'u') in that word.
def getVowels(word):
	l = ['a','e','i','o','u','A','E','I','O','U']
	l1=[]
	for i in range(0,len(word)):
		if word[i] in l:
			l1.append(word[i])
	return l1

word = input("Enter The string to get all vowel list in the string : ")
print("total vowel in that word is = ",getVowels(word))