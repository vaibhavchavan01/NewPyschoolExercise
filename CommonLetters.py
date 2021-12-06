# Write the function getCommonLetters(word1, word2) that 
# takes in two words as arguments and returns a new string that contains letters found in both string. 
# Ignore repeated letters and sort the result in alphabetical order.
def getCommonLetters(word1, word2):
	str=""
	l=[]
	for i in range(0,len(word1)):
		if word1[i] in word2 and word1[i] not in l:
			l.append(word1[i])
	l = sorted(l)
	for i in l:
		str+=i
	return str
word1=input("Enter the first word : ")
word2=input("Enter the second word : ")
print("common latters in given words is = ",getCommonLetters(word1,word2))