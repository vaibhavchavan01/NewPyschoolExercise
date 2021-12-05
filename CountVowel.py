# Write a function countVowels(word) 
# that takes in a word as an argument and returns 
# the number of vowels ('a', 'e', 'i', 'o', 'u') in the word.
def countVowels(word):
	l1=['a','e','i','o','u']
	cnt=0
	for i in range(0,len(word)):
		if word[i] in l1:
			cnt+=1
	return cnt
word = input("Enter The word to count vowel in word : ")
print("total vowel in the word is = ",countVowels(word))
