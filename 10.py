import math
def is_prime(number):
	#print number
	iterator_end = int(round(math.sqrt(number))+1)
	#print iterator_end
	for n in range(2, iterator_end):
		if number % n == 0:
			return False
	return True
def prime():
	primes = [2]
	number = 3
	while True:
		if number <= 2000000:
			if is_prime(number):#2000000:
				#print number
				primes.append(number)
		else:
			return sum(primes)
		number += 2
print prime()