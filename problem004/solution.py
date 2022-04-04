import datetime as dt
def isPalindrome(x):
    xStr = str(x)
    return xStr == xStr[::-1]

def maxNDigitProductPalindrome(n):
    digitRange = range(10**n, 10**(n-1), -1)
    maxPalindromes = []

    ## can probably insert a break clause somewhere?
    for x in digitRange:
        xPalindromes = [(x, y, x*y) for y in digitRange if isPalindrome(x*y)]
        if len(xPalindromes) > 0:
            maxPalindromes.append(max(xPalindromes, key=lambda p: p[2]))
    return max(maxPalindromes, key=lambda p: p[2])

### pre
t0 = dt.datetime.now()


### SOLUTION HERE
solution = maxNDigitProductPalindrome(3)[2]


#### post
t1 = dt.datetime.now()
seconds = (t1 - t0).microseconds / 10**6
print("##########")
print(f"SOLUTION FOUND IN {seconds} SECONDS")
print(f"SOLUTION: {solution}")
    
