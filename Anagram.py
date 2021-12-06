# An anagram is a word formed by reordering the letters of another word. Write a function isAnagram(w1, w2) 
# that takes in two words as arguments and return True if one word is an anagram of the other word.
def isAnagram(w1, w2):
	str1=w1.lower()
	str2=w2.lower()
	if len(str1)!=len(str2):
		return False
	for i in str1:
		if i not in str2:
			return False
	return True
word1=input("Enter the first word : ")
word2=input("Enter the second word : ")
print(isAnagram(word1,word2))