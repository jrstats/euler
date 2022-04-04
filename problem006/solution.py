import datetime as dt
import math

### pre
t0 = dt.datetime.now()


### SOLUTION HERE
solution = sum([x for x in range(1,100+1)])**2 - sum([x**2 for x in range(1,100+1)])


#### post
t1 = dt.datetime.now()
seconds = (t1 - t0).microseconds / 10**6
print("##########")
print(f"SOLUTION FOUND IN {seconds} SECONDS")
print(f"SOLUTION: {solution}")
    
