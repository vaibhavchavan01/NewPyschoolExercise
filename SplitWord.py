# Write a function splitWord(word, numOfChar) that takes in a word and a number as arguments. 
# The function will split the word into smaller segments with 
# each segment containing the number of letter specified in the numOfChar argument. 
# These segments are stored and returned in a list.
def splitWord(word, numOfChar):
	l=[]
	str1=""
	start=0
	end=numOfChar
	for i in range(0,len(word)):
		if str1 != word:
			l.append(word[start:end])
			str1+=word[start:end]
			start=end
			end=start+numOfChar
		else:
			break
	return l
word=input("Enter the Word to split : ")
num=int(input("Enter how many character in split : "))
print(splitWord(word,num)) 