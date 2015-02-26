def isMultipleOf(tall, bases):
    for base in bases:
        if tall % base == 0:
            return True
    return False

def multiples(grense, bases):
    svar = 0
    for tall in range(grense):
        #print 'tall', tall
        if isMultipleOf(tall, bases):
            svar += tall
            #print 'svar', svar
    return svar

def main():
    grense = 1000
    bases = [3, 5]
    print 'svar: ', multiples(grense, bases)
main()
                
