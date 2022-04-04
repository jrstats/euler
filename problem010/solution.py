import datetime as dt
import math
def generateIsPrime(n):
    # Eratosthenes Seive
    # https://www.youtube.com/watch?v=JA_YrFwE1hc
    if n < 2:
        return []
    
    # generate list of 0, 1, 2, 3,  ..., n
    nArray = [False, False] + [True] * (n-1)
    maxCheck = math.isqrt(n) + 1
    for i in range(2, maxCheck):
        if nArray[i]:
            for j in range(i**2, n+1, i):
                nArray[j] = False
    return nArray

def generatePrimesLeqN(n):
    return [i for i, x in enumerate(generateIsPrime(n)) if x]

def setOfPrimeFactors(x):
    possiblePrimeFactors = generatePrimesLeqN(math.isqrt(x)+1)
    return {y for y in possiblePrimeFactors if x % y == 0}

def primeFactorisation(x):
    primeFactorisation = []
    primeFactors = setOfPrimeFactors(x)
    xCheck = x
    for p in primeFactors:
        while xCheck % p == 0:
            primeFactorisation.append(p)
            xCheck = xCheck / p
    return primeFactorisation

### pre
t0 = dt.datetime.now()


### SOLUTION HERE
solution = sum(generatePrimesLeqN(2_000_000))


#### post
t1 = dt.datetime.now()
seconds = (t1 - t0).microseconds / 10**6
print("##########")
print(f"SOLUTION FOUND IN {seconds} SECONDS")
print(f"SOLUTION: {solution}")
    
