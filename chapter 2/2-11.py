#binomial coefficients
from math import factorial
from numpy import array

def binomial(n,k):
    if(k == 0):
        return 1;
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

for n in range(1, 21):
    results = [];
    for k in range(0, n+1):
        results.append(binomial(n, k));
    print(results);