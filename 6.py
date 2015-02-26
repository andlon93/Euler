def sum_of_squares(i):
	n = 0
	b = 0
	for k in xrange(1,i+1):
		n += k**2 
		b += k
	b = b**2
	print b
	print n
	print b-n
sum_of_squares(100)
