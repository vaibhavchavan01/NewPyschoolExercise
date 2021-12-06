# Write a function calCumulativeSum(numbers) that takes in a 
# list of numbers as argument and returns the cumulative sum of the list. That is, 
# the new list where the i element is the sum of the first i + 1 elements from the original list. 
# For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
def calCumulativeSum(numbers):
	l = []
	sum=0
	for i in numbers:
		sum+=i
		l.append(sum)
	return l 
print(calCumulativeSum([2,2,2]))