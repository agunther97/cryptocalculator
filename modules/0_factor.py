from functools import reduce

def factor_prime(nr):
    i = 2
    factors = []
    while i <= nr:
        if (nr % i) == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    return factors #(factor,factor,factor2)

def factor_prime_tuple(nr):
    facs=factor_prime(nr)
    factors={}
    for fac in facs:
        if fac in factors:
            factors[fac]+=1
        else:
            factors[fac]=1
    tupleFactors=[]
    for k,v in factors.items():
        tupleFactors.append((k,v))
    return tupleFactors #[(factor, exponent),(factor2,exponent)]

def factor(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))