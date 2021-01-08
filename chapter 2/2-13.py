#recursion
def catalan(n):
    if(n == 0):
        return 1
    else:
        return (((4*n) - 2) / (n + 1)) * catalan(n-1);

#greatest common divisor
def g(m, n):
    if(n == 0):
        return m;
    else:
        return g(n, m % n);

print(g(108, 192));