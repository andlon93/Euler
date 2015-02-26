def evenlydivisors(number):
	d_number = 0
	for n in xrange(1, (number/2)+1 ):
		if number % n == 0:
			d_number += n
	is_amicable = 0
	for n in xrange(1, (d_number/2)+1 ):
		if d_number % n == 0:
			is_amicable += n
	if number == is_amicable and d_number != is_amicable:
		return True, d_number
	else:
		return False, d_number
def iterate(number):
	summ = 0
	teller = 1
	while teller <= number:
		b, v = evenlydivisors(teller)
		if b:
			summ += teller + v
			teller = v
		teller += 1
	return summ
print iterate(20000)
''' Svar: 31626
    [Finished in 6.0s]'''