# Write the function capitalizeVowels(word) 
# that returns the word with all the vowels capitalized.
def capitalizeVowels(word):
	str=""
	l=['a','e','i','o','u']
	for i in range(0,len(word)):
		if word[i] in l:
			str=str+word[i].capitalize()
		else:
			str=str+word[i]
	return str
word = input("Enter the word to capitalize the vowel : ")
print("After capitalize of vowel in the word = ",capitalizeVowels(word))