'''If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
   If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?'''
def enerplass(streng):
	if streng == '1':    return 'one'
	elif streng == '2':  return 'two'
	elif streng == '3':  return 'three'
	elif streng == '4':  return 'four'
	elif streng == '5':  return 'five'
	elif streng == '6':  return 'six'
	elif streng == '7':  return 'seven'
	elif streng == '8':  return 'eight'
	elif streng == '9':  return 'nine'
	elif streng == '10': return 'ten'
	elif streng == '11': return 'eleven'
	elif streng == '12': return 'twelve'
	elif streng == '13': return 'thirteen'
	elif streng == '14': return 'fourteen'
	elif streng == '15': return 'fifteen'
	elif streng == '16': return 'sixtenn'
	elif streng == '17': return 'seventeen'
	elif streng == '18': return 'eighteen'
	elif streng == '19': return 'nineteen'
	else: return ''
def foo(streng):
	if streng == '0': return 'ten'
	elif streng == '1': return 'eleven'
	elif streng == '2': return 'twelve'
	elif streng == '3': return 'thirteen'
	elif streng == '4': return 'fourteen'
	elif streng == '5': return 'fifteen'
	elif streng == '6': return 'sixtenn'
	elif streng == '7': return 'seventeen'
	elif streng == '8': return 'eighteen'
	elif streng == '9': return 'nineteen'
def tierplass(s):
	if s == '2':   return 'twenty'
	elif s == '3': return 'thirty'
	elif s == '4': return 'forty'
	elif s == '5': return 'fifty'
	elif s == '6': return 'sixty'
	elif s == '7': return 'seventy'
	elif s == '8': return 'eighty'
	elif s == '9': return 'ninety'
	else: return ''	
def plasser(number):
	s = str(number)
	svar = ''
	if number < 20: 
		return enerplass(s)
	elif number < 100: 
		return tierplass(s[0]) + enerplass(s[1])
	elif number < 1000:
		svar += enerplass(s[0])
		svar += 'Hundred'
		if s[1] != '0':
			svar += 'and'
			if s[1] == '1':
				svar += foo(s[2]) 
				return svar
			else:
				svar += tierplass(s[1])
			if s[2] != '0':
				svar += enerplass(s[2])
		elif s[2] != '0':
			svar += 'and' 
			svar += enerplass(s[2])
		return svar
	else:
		return 'OneThousand'
lengde = 0
temp = ''
for n in xrange(1,1001):
	temp = plasser(n)
	#print temp, len(temp)
	lengde += len(temp)
print lengde
''' svar: 21124
    [Finished in 0.1s] '''