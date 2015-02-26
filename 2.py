def fibonacci(maks):
    fibNumbers = []
    while fibNumbers == [] or fibNumbers[-1] <= maks:
        n = len(fibNumbers)
        if n == 0:
            fibNumbers.append(1)
        elif n == 1:
            fibNumbers.append(2)
        else:
            nytt = fibNumbers[n-1] + fibNumbers[n-2]
            if nytt <= maks:
                fibNumbers.append(nytt)
            else:
                return fibNumbers
def evenNumbers(n):
    liste = []
    for i in n:
        if i % 2 == 0:
            liste.append(i)
    return liste
def summ(liste):
    svar = 0
    for n in liste:
        svar += n
    return svar       
def main():
    maks = 4000000
    fib = fibonacci(maks)
    evenFib = evenNumbers(fib)
    svar = summ(evenFib)
    print 'Alle fibonacci-tall som er mindre enn', maks, ' :\n', fib
    print '-------------------------------------------------------'
    print '\nAlle som er partall: \n', evenFib
    print '-------------------------------------------------------'
    print '\nSummen av alle som er partall: ', svar
main()
