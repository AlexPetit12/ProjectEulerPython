"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

# basic implementation of Sieve of Eratosthenes algorithm
def nth_prime(n, length):
    # generate a list of integers from 2 to n
    int_list = list(range(2, length + 1))
    
    pos = 0 # position of multiple of prime 
    to_remove = int_list[pos] # multiple to remove
    
    while(to_remove * to_remove <= max(int_list)):
        for integer in int_list:
            if (integer != to_remove) and (integer % to_remove == 0):
                int_list.remove(integer)
        pos += 1
        to_remove = int_list[pos]
    
    return int_list[n - 1]

print(nth_prime(10001, 125000))
    