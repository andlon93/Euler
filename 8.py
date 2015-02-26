from sys import stdin
def multiply(tall_list):
	produkt = 1
	for tall in tall_list:
		produkt *= tall
	return produkt
def lag_liste(size):
	list = []
	hoyest = 0
	temp_hoyest = 0
	for line in stdin.readline().split():
		for digit in line:
			list.append(int(digit))
	multiply_list = list[0:size]
	for n in xrange(size+1,1000):
		multiply_list.pop(0)
		multiply_list.append(list[n])
		temp_hoyest = multiply(multiply_list)
		if  temp_hoyest > hoyest:
			hoyest = temp_hoyest
	return hoyest 
print lag_liste(13)