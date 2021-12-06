# Write a function getEvenNumbers(numbers) to return all the even numbers in a list.
def getEvenNumbers(numbers): 
	l=[]
	for i in numbers:
		if i%2==0:
			l.append(i)
	return l
print(getEvenNumbers(range(1, 20, 3)))