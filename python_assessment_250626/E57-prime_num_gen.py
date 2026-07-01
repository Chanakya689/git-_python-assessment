#Given Input: Range: 10 to 50
#Expected Output: Primes: [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

from random import randint

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

primes = [num for num in range(10, 51) if is_prime(num)]
print(f"Primes: {primes}")