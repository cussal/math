
from random import randint
import math

n = int(input("How many prizes do you need?\n"))
iters = 100000

count = 0
theoretical = 0

for i in range(iters):
	remaining = set(range(1,n+1))
	while(remaining):
		integer = randint(1,n)
		remaining.discard(integer) 
		count += 1

numerical = count/iters 

for i in range(1,n+1):
	theoretical += n / i

euler = n*math.log(n) + 0.5772156649*n + 0.5


print("Numerical solution:   ", round(numerical,4))

print("Theoretical Solution: ", round(theoretical,4))

print("Euler Approximation:  ", round(euler,4))

#print("Difference:           ", round(abs(theoretical - numerical),4))
