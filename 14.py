even = lambda x: x/2
odd = lambda x: (x*3)+1
def make_sequence(number):
	teller = 1
	while number != 1:
		if number % 2 == 0:
			number = even(number)
		else:
			number = odd(number)
		teller += 1
	return teller
def main():
	q = 500001
	z = 1000001
	hoyest = (0, -1)		
	temp = 0
	for n in range(q,z):
		temp = make_sequence(n)
		#print 'temp', temp
		if temp > hoyest[0]:
			hoyest = (temp, n) 
			#print hoyest
	print 'hoyeste er: ', hoyest[1]
main()#27.3 s

