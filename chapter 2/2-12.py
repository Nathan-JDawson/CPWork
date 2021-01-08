#prime nummbers
from math import sqrt

primes = [2];

for n in range(3, 1000000):
    for p in primes:
        if(p > sqrt(n)):
            primes.append(n);
            break;
        if(n % p == 0):
            break;
print(primes);
        