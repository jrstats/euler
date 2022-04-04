import datetime as dt
import math

### pre
t0 = dt.datetime.now()


### SOLUTION HERE
solution = math.lcm(*range(1, 20+1))


#### post
t1 = dt.datetime.now()
seconds = (t1 - t0).microseconds / 10**6
print("##########")
print(f"SOLUTION FOUND IN {seconds} SECONDS")
print(f"SOLUTION: {solution}")
    
