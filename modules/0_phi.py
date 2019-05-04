def phi(n,verbose=False):
    primes=factor_prime_tuple(n)
    total=1
    if verbose:
        print("Prime factorization:")
        s=""
        for tup in primes:
            s+=str(tup[0])+superscript(tup[1])+"*"
        s=s[:-1]
        print(s)
    s=""
    for tup in primes:
        p=tup[0]
        e=tup[1]
        total=total*( pow(p,e) - pow(p,e-1) )
        s+="("+str(p)+superscript(e)+"-"+str(p)+superscript(e-1)+")*"
    s=s[:-1]
    if verbose:
        print(totient+"="+s)
    return total

registerFunction("phi", {
    "name" : "Phi",
    "arguments_short":["n","verbose=False"],
    "arguments":["number","print commands"],
    "description":"Computes Euler's totient of a number"
})