import sympy
if __name__ == "__main__":
    print("The 5th prime is:",sympy.prime(5))
    print("The 13th prime is:",sympy.prime(13))
    print("Is 5 a prime number:",sympy.isprime(5))
    print("Is 6 a prime number:",sympy.isprime(6))
    print(
        "The prime numbers between 0 & 100 are:",
        list(sympy.primerange(0, 100)),sep="\n"
    )
    print(
        "The prime numbers between 0 & 100 are(Using Sieve):",
        list(sympy.sieve.primerange(0, 100)),sep="\n"
    )
    print("A random prime between 0 & 100:", sympy.randprime(0, 100))
    print("A random prime between 0 & 100:", sympy.randprime(0, 100))
    print("The largest prime less than 50 is:", sympy.prevprime(50))
    print("The smallest prime greater than 50 is:", sympy.nextprime(50))