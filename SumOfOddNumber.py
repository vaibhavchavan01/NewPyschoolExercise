# Write a function addOddNumbers(numbers) to add all the odd numbers in a list. 
# To access each element in a list, you can use the statement 'for num in numbers:'.
def addOddNumbers(numbers): 
	sum = 0
	for i in numbers:
		if i%2!=0:
			sum+=i
	return sum

print(addOddNumbers(range(1, 20, 3)))