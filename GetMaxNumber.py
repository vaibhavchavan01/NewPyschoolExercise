# Write a function getMaxNumber(numbers) that returns the maximum number in a list.
def getMaxNumber(numbers):
	max=0 
	if len(numbers)>0:
		for i in numbers:
			if i>max:
				max=i
		return max
	else:
		return 'N.A'
print(getMaxNumber([1, 4, 8, 50, 10]))