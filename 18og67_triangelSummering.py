fil = open('67_input.txt', 'r')
def lag_matrise():
	matrix = []
	list = []
	s = ''
	for line in fil:
		for tegn in line:
			s += tegn
			if tegn == ' ':
				list.append( int(s[0:-1]) )
				s = ''
			elif '\n' in s:
				list.append( int(s[0:-1]) )
				matrix.append(list)
				s = ''
				list = []
	matrix.append(list)
	return matrix
def main():
	matrix = lag_matrise()
	n = len(matrix)
	for rad in xrange(n-1,0,-1):
		for index in xrange(0, len(matrix[rad])-1 ):
			matrix[rad-1][index] += max(matrix[rad][index], matrix[rad][index+1])
	return matrix[0]
print main()
fil.close()

''' oppgave 18:
	svar: 1074
	[Finished in 0.1s]

	oppgave 67:
	svar: 7273
	[Finished in 0.2s]'''