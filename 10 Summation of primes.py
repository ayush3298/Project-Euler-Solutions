def primes_method5(n):
    out = list()
    s = 0
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p]):
            s = s+p
            for i in range(p, n+1, p):
                sieve[i] = False
    return s
print(primes_method5(2000000))
