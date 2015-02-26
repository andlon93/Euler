def word_value(word):
	value = 0
	for letter in word:
		if letter == "#": value += 0
		elif letter == "A": value += 1
		elif letter == "B": value += 2
		elif letter == "C": value += 3
		elif letter == "D": value += 4
		elif letter == "E": value += 5
		elif letter == "F": value += 6
		elif letter == "G": value += 7
		elif letter == "H": value += 8
		elif letter == "I": value += 9
		elif letter == "J": value += 10
		elif letter == "K": value += 11
		elif letter == "L": value += 12
		elif letter == "M": value += 13
		elif letter == "N": value += 14
		elif letter == "O": value += 15
		elif letter == "P": value += 16
		elif letter == "Q": value += 17
		elif letter == "R": value += 18
		elif letter == "S": value += 19
		elif letter == "T": value += 20
		elif letter == "U": value += 21
		elif letter == "V": value += 22
		elif letter == "W": value += 23
		elif letter == "X": value += 24
		elif letter == "Y": value += 25
		else: value += 26
	return value
###############################################
def lag_liste():
	temp = open('22_input.txt', 'r')
	navnliste = []
	list = []
	#SLUTT - definere lokale variabler

	#START - lage liste med navn
	for line in temp:
		list = line.split(',')
	for word in list:
		word = word[1:-1]#fjerne " " fra strengene
		navnliste.append(word)
	return navnliste
################################################
def main():
	navnliste = sorted( lag_liste() ) #sorter liste med alle navn
	return sum( (n+1) * word_value( navnliste[n] ) for n in xrange (0, len(navnliste) ) )#sum(namescores)
'''
871198282
[Finished in 0.2s]
'''