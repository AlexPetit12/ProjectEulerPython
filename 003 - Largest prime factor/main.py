"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def isPrime(n):
    if n == 2: return True
    if n == 3: return True
    if n % 2 == 0: return False
    if n % 3 == 0: return False

    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True

i = 1
n = 600851475143 
while True:
    if n % i == 0:
        if isPrime(n / i):
            break;
    i += 2
        
print(n / i)