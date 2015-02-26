import math
def divisors(number):
	divisors = 0
	teller = 1
	while teller <= math.sqrt(number):
		if number % teller == 0:
			divisors += 2
		teller += 1
	#print 'lengde', divisors
	return divisors
def triangle_number(ant_divisors):
	number = 1
	teller = 2
	while divisors(number) <= ant_divisors:
		number += teller
		teller += 1
		#rint 'number', number
	return number
print triangle_number(500)