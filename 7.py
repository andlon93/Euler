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
	teller = 6
	test_tall = 15
	while True:
		if is_prime(test_tall):
			teller += 1
			#print teller, test_tall
			if teller == 10001:
				return test_tall
		test_tall += 1
print prime()