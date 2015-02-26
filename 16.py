'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
'''
summ = 0
tall = 2**1000
streng = str(tall)
for tall in streng:
	summ += int(tall)
print summ
'''
svar: 1366
tid: 0.1 s
'''