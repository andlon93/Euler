'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
def calculateDay(year, month):
	if month == 9 or month == 4 or month == 6 or month == 11: 
		dager = 30
	elif month == 2: # start Februar
		if year % 4 == 0: 
			dager = 29
			if year % 100:
				if not year % 400: 
					dager = 29
				else: 
					dager = 28
		else: 
			dager = 28 #slutt Februar
	else: 
		dager = 31 #Funnet antall dager i den gitte maaned
	return dager % 7 #Returnerer hvilken dag 1. neste maaned er
def main():
	dag = 2
	teller = 0
	for year in xrange(1901,2001):
		for month in xrange(1,13):
			dt = calculateDay(year, month)
			#print month, dag, dt
			if dt+dag > 7:
				okning_fra_mandag = (dt+dag) - 7
				dag = okning_fra_mandag
			else:
				dag += dt
			if dag == 1:
				teller += 1
	print teller
main()
'''
171
[Finished in 0.2s]
'''