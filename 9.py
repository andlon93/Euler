def main():
	for a in xrange(1,999):
		for b in xrange(1,500):
			c = 1000 - a - b
			if (a**2 + b**2 == c**2):
				return a, b , c, a*b*c
print main()
