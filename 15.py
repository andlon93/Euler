'''
6 3 1
3 2 1
1 1 0
2x2
'''
def print_matrix(matrix):
	for line in matrix:
		for e in line:
			print e, '\t\t',
		print ''
def lag_matrise():
	matrix = []
	for x in xrange(0,21):
		list = [0]*21
		matrix.append(list)
	for x in xrange(0,21):
		matrix[20][x] = 1
		matrix[x][20] = 1
	matrix[20][20] = 0 
	return matrix
def main():
	matrix = lag_matrise()
	n = len(matrix)
	print n
	for x in xrange(n-2,-1,-1):
		matrix[x][x] = matrix[x+1][x] + matrix[x][x+1]
		index = x
		for n in xrange(index-1,-1,-1):
			matrix[index][n] = matrix[index+1][n] + matrix[n+1][index]
			matrix[n][index] = matrix[n+1][index] + matrix[n][index+1]
	print_matrix(matrix)
main()#0.2 s