def is_prime_det(num):
    '''Calculates whether num is a prime number,
    if it is return True otherwise return Flase'''

    try:
        int(num)
    except ValueError:
        raise ValueError("Ops. Input must be a positive integer")
    if int(num) != num or num < 0:
        raise ValueError("Ops. Input must be a positive integer")

    # SPECIALCASE: These are special cases that are not primes
    if num in [0, 1]: return False

    primes_to_remove = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for prime in primes_to_remove:
        if num == prime: return True
        elif num % prime == 0: return False

    # Look for a factor
    limit = int(num**(0.5))+1
    for multiple in range(30, int(num**(0.5))+1, 30):
        for k in [1, 7, 11, 13, 19, 23, 29]:
            # If there is a factor
            if num % (multiple+k) == 0:
                # Its not a prime number
                return False
    return True

try:
    import numpy as np

    def primesbelow(n):
        sieve = np.ones(n//3 + (n%6==2), dtype=np.bool)
        sieve[0] = False
        for i in range(int(n**0.5)//3+1):
            if sieve[i]:
                k=3*i+1|1
                sieve[      ((k*k)//3)      ::2*k] = False
                sieve[(k*k+4*k-2*k*(i&1))//3::2*k] = False
        return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]


    smallprimeset = set(primesbelow(100000))
    _smallprimeset = 100000

    def is_prime(n, fast=False, precision=100):
        if (not fast) and (len(str(n))<18):
            return is_prime_det(n)
        try:
            n = abs(int(n))
        except ValueError:
            print("Input must be a non-negative integer")
        if n in [0, 1]:
            return False
        elif n in [2, 3, 5]:
            return True
        elif n % 2 == 0:
            return False
        elif n < _smallprimeset:
            return n in smallprimeset

        # Miller-Rabin primality test

        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1

        for repeat in range(precision):
            a = random.randrange(2, n - 2)
            x = pow(a, d, n)

            if x == 1 or x == n - 1: continue

            for r in range(s - 1):
                x = pow(x, 2, n)
                if x == 1: return False
                if x == n - 1: break
            else: return False
        return True
except Exception as inst:
    print("No numpy!")
    print(type(inst))
    print(inst.args)
    print(inst)
    def is_prime(n):
        return is_prime_det(n)