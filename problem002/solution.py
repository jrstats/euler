import datetime as dt

def nth_fibinacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return nth_fibinacci(n-1) + nth_fibinacci(n-2)

### pre
t0 = dt.datetime.now()


### SOLUTION HERE
x = 100
solution = 0
for n in range(1, x):
    fib_n = nth_fibinacci(n)
    if fib_n > 4_000_000:
        print(f"{n}th fibonacci is {fib_n} > 4m")
        print("stopping")
        break
        
    if fib_n % 2 == 0:
        solution += fib_n


#### post
t1 = dt.datetime.now()
seconds = (t1 - t0).microseconds / 10**6
print("##########")
print(f"SOLUTION FOUND IN {seconds} SECONDS")
print(f"SOLUTION: {solution}")
    
