# Write a function (list1, list2) that takes in two lists as arguments and 
# return a list that is the result of removing elements from list1 that can be found in list2.
def subtractList(list1, list2): 
	l=[]
	for i in list1:
		if i not in list2:
			l.append(i)
	return l
print(subtractList([1,2,3,4,5], [2, 4]))