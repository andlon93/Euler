def is_divisible(number):
	for i in xrange(2,21):
		if not number % i == 0:
			return False
	return True
def iterator():
	number = 20
	while True:
		if is_divisible(number):
			return number
		number += 2
print iterator()