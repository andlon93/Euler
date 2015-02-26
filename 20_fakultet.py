def summ(tall):
	s = str(tall)
	svar = 0
	for siffer in s:
		svar += int( siffer )
	return svar

def fakultet(number):
	produkt = 1
	while number != 0:
		produkt = produkt*number
		number -= 1
	return produkt

print summ( fakultet(100) )
'''
648
[Finished in 0.1s]
'''