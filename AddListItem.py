# Write a function addNumbersInList(numbers) to add all the numbers in a list. 
# To access each element in a list, you can use the statement 'for num in numbers:
def addNumbersInList(numbers):
	sum=0 
	if len(numbers)>0:
		for i in numbers:
			sum+=i
		return sum 
	else:
		return 0

print(addNumbersInList([10, 20, 30]))