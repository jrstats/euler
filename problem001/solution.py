import datetime as dt

t0 = dt.datetime.now()
solution = sum([x for x in range(1, 1000) if (x % 3 == 0) or (x % 5 == 0)])
t1 = dt.datetime.now()

seconds = (t1 - t0).microseconds / 10**6

print("##########")
print(f"SOLUTION FOUND IN {seconds} SECONDS")
print(f"SOLUTION: {solution}")
    
