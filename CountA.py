"""Write the function countA(word) that takes in a 
word as argument and returns the number of 'a' in that word."""
def countA(word):
	cnt=0
	for i in range(0,len(word)):
		if word[i]=='a':
			cnt+=1
	return cnt
str=input("Enter The String to count no of 'a' in that string : ")
print("Total 'a' in given string is = ",countA(str))