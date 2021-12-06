# Write a function isTripleDouble(word) that 
# takes in a word as argument and returns True 
# if the word contains three consecutive double letters.
def isTripleDouble(word):
	flag=cnt=0
	for i in range(0,len(word)-4):
		if word[i]==word[i+1]:
			if word[i+2]==word[i+3]:
				cnt+=1
				if cnt==2:
					flag=0
					break
			else:
				flag=1
				break
		elif((len(word)-1<6) and (cnt>1)):
			flag=1
			break
	if flag==0 and cnt==2:
		return True
	else:
		return False
word = input("Enter The word : ")
print(isTripleDouble(word))