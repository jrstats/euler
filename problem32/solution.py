# %% [markdown]
# # [Problem 32](https://projecteuler.net/problem=32)

# %% [markdown]
# 
# 
# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# 
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# 
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
# 

# %%
import datetime as dt

# %%
def intToStrSet(x):
    return str(x), set(str(x))

def isPandigital(x):
    xStr, xSet = intToStrSet(x)

    if len(xStr) != 9:
        return False

    if contains0(xStr, xSet):
        return False
    
    if containsDuplicate(xStr, xSet):
        return False

    return containsAllDigits(xStr, xSet)

    
def contains0(xStr, xSet):
    return "0" in xStr

def containsDuplicate(xStr, xSet):
    return len(xSet) != len(xStr)


def containsAllDigits(xStr, xSet):
    return xSet == set([str(y) for y in range(1, len(xStr)+1)])


# %%
def productToStr(a, b):
    return f"{a} * {b} = {a*b}"

def productLen(a, b):
    return len(str(a) + str(b) + str(a*b))

def productIsPandigital(a, b):
    if (contains0(*intToStrSet(a)) or 
        contains0(*intToStrSet(b)) or 
        contains0(*intToStrSet(a*b)) or 
        containsDuplicate(*intToStrSet(a)) or 
        containsDuplicate(*intToStrSet(b)) or
        containsDuplicate(*intToStrSet(a*b))
    ):
        return False, None

    xStr = str(a) + str(b) + str(a*b)
    if isPandigital(xStr):
        print(productToStr(a, b))
        return True, a*b
    else:
        return False, None

# %%
def findPandigitalProducts():
    pandigitalProducts = []
    for a in range(2, 10**9):
        maxB = int((10**9)/a)
        if productLen(a, a) > 9:
            break
        for b in range(a, maxB):
            if productLen(a, b) > 9:
                break
            pIsPandigital, product = productIsPandigital(a, b)
            if pIsPandigital:
                pandigitalProducts.append(product)
    return pandigitalProducts

# %%
t0 = dt.datetime.now()


pandigitalProducts = findPandigitalProducts()
pandigitalProductsSet = set(pandigitalProducts)

t1 = dt.datetime.now()
t2 = t1 - t0

print("##########")
print(f"SOLUTION FOUND IN {t2.microseconds / 10**6} SECONDS")
print(f"NUMBER OF SOLUTIONS: {len(pandigitalProducts)}")
print(f"NUMBER OF UNIQUE SOLUTIONS: {len(pandigitalProductsSet)}")
print(f"SUM: {sum(pandigitalProductsSet)}")
    


