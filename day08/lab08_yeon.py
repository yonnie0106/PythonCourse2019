## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(x, y):
    while x % y != 0:
        x, y = y, x%y 
    return y 

print(gcd(14, 18))
        
    


## Problem 2
## Write a function using recursion that returns prime numbers less than 121
def find_primes(me = 121, primes = []):
	for i in range(2, me):
		isPrime = True
		for j in primes:
			if i % j == 0:
				isPrime ==False
				break
			elif j > i**0.5:
				 break 
			
				continue
			return True

find_primes(18, primes= [])

 
## Problem 3
## Write a function that gives a solution to Tower of Hanoi game
## https://www.mathsisfun.com/games/towerofhanoi.html
