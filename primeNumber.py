def primeNumbers(num):
    primes = [] 
    i = 2
    # iterates through range from 2 to num(inclusive)
    while i <= num:     # add 'while' condition
        k = 2
        isPrime = 1
        # check if prime number
        while k < i:      # add 'while' condition
	if i%k== 0:
	    isPrime = 0
	    break
    k += 1           # update k
    if isPrime == 1:
        primes.append(i)
    i += 1              # update i
    return primes 
print(primeNumbers(5))