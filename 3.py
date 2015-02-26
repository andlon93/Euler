def primtall(maks):
    prime = []
    for tall in range(1,maks):
        prime.append(tall)
        isPrime = True 
        for n in range(2,tall):
            if tall % n == 0:
                isPrime = False
        if not isPrime:
            prime.pop()
    return prime
#
def primeFactors(tall, primes):
    primeFactor = []
    for prime in primes:
        if tall % prime == 0:
            primeFactor.append(prime)
            if tall == prime:
                return primeFactor[-1]
            tall = tall/prime
#
def main():
    faktor = 600851475143
    print 'Faktoriserer', faktor, '\n'
    primes = primtall(7000)
    print 'Storste primtall i faktoriseringen er: ', primeFactors(faktor, primes)
main()

        
