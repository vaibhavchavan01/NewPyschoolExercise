def fibonacci(number):
	
	if number ==0 or number == 1:
		return number
	else:
		#c+=1
		return fibonacci(number-1) + fibonacci(number-2)
n1 = int(input("enter the number: "))

print(fibonacci(n1))