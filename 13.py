'''
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
'''
from sys import stdin 

def lag_liste():
	numbers = []
	for line in stdin.readlines():
		n = len(line)
		if '\n' in line:
			line = line[0:-1]
		numbers.append( line )

	summ = 0
	for tall in numbers:
		summ += int(tall)
	summ = str(summ)
	#print summ
	print summ[0:10]
lag_liste()