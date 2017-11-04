import time
import math

#numerical square root finder
square = int(input())
sq_digits = 4
t_digits = 4
epsilon = 0.01

# first method is just to use the math function!
print("Math Library: ", round(math.sqrt(square),sq_digits))

up_bound = square
low_bound = 0

n = square/2

start = time.time()

# We then use an optimized technique
counter = 0
while((square - epsilon > n*n) or (n*n > square + epsilon)):
    counter += 1
    
    if((n > low_bound) and (square - epsilon > n*n) ):
        low_bound = n
    elif((n < up_bound) and (n*n > square + epsilon)):
        up_bound = n
    
    n = (low_bound+up_bound)/2

print("Optimized:    ", round(n,sq_digits), "which took",round(time.time()-start,t_digits),"seconds and", counter, "checks")
start = time.time()


# Brute force is pretty bad...
i = 0
counter = 0
while (i <= square):
    counter += 1
    if(square - epsilon < i*i < square + epsilon):
        break
    i += 0.0001



print("Brute Force:  ", round(i,sq_digits), "which took",round(time.time()-start,t_digits),"seconds and", counter, "checks")



