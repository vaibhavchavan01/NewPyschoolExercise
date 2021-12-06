def gcd(a, b):
	if a==0:
		return b
	elif b==0:
		return a
	elif a==b:
		return a
	elif a>b:
		return  gcd(a-b, b)
	else:
		return gcd(a, b-a)
n1 = int(input("enter the number: "))
n2 = int(input("enter the number: "))

print(gcd(n1, n2))