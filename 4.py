def is_palindrome(number):
	tall = str(number)
	reverse_tall = ''
	list = []
	for siffer in tall:
		list.append(siffer)
	for index in range(len(list)-1,-1,-1):
		reverse_tall += list[index]
	if tall == reverse_tall:
		return True
def product():
	list = []
	for tall1 in range(999,899,-1):
		for tall2 in range(999,899,-1):
			print tall1, tall2
			svar = tall1*tall2
			if is_palindrome(svar):
				list.append(svar)
	return max(list)
print product()