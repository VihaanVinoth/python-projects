import random 
import math 

num1 = random.randint(1, 6) 
num2 = random.randrange(10, 50, 5) 
numfloat = random.uniform(1, 10) 

squarenum = math.sqrt(num1 + num2 + numfloat) 
squarefloor = math.floor(squarenum) 
squareceil = math.ceil(squarenum) 

print(f"{squarenum} is the square root") 
print(f"{squarefloor} is the floor of {squarenum}") 
print(f"{squareceil} is the ceiling of {squarenum}") 

 