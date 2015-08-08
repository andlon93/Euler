'''
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import math
debug = False

def lex_numbers_given_digits(n): 
	return math.factorial(n)/n

def update_list(old_list, c, p):
	new_list=[]

	for n in range(0, len(old_list)):
		if n < c: new_list.append( old_list[n] )
		elif n==c: new_list.append( old_list[p+c] )
		elif n > c and n <= (p+c): new_list.append( old_list[n-1] )
		elif n > (p+c): new_list.append( old_list[n] )

	return new_list


def main(digits, goal_permutation):
	n = len(digits)
	
	current_permutation = 1
	counter = 0

	while current_permutation < goal_permutation:
		if debug: 
			print "N ", n
			print "counter: ", counter
		delta = math.factorial(n-1) #okning per tall i gitt posisjon
		if debug: print "delta: ", delta 

		permutations = (goal_permutation - current_permutation) / delta	
		if debug: print "permutations: ", permutations
		
		digits = update_list(digits, counter, permutations)
		if debug: print "updated digits: ", digits

		current_permutation += permutations*delta
		if debug: print "current_permutation: ", current_permutation
		
		n -= 1
		counter += 1
		if current_permutation == goal_permutation: return digits
	return digits

def to_int(list):
	answer = ""
	for n in list: answer += str(n)
	return answer

#print to_int( main([0, 1, 2, 3], 7) )
print  to_int( main([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 1000000) )
'''
Answer: 2783915460
runtime: [Finished in 0.1s]
'''