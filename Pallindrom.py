# A palindrome is a word, phrase, number or other sequence of units that can be read the same way in either direction. 
# Write a function that determines whether the given word or number is a palindrome
def isPalindrome(num):
	flag=0
	i=0
	j=len(num)-1
	if j<1:
		return False
	while i<=j//2:
		if num[i]!=num[j]:
			flag=1
			break
		else:
			i+=1
			j-=1
	if flag==1:
		return False
	else:
		return True 
word=input("Enter The sequence to check is pallindrom or not : ")
print(isPalindrome(word))