import math

def rsa_pq(n,verbose=False):
    if verbose:
        print("Factoring n to p*q")
    p = math.floor(math.sqrt(n))
    if verbose:
        print(indentStr+"floor(sqrt("+str(n)+"))="+str(p))
    if p % 2 == 0:
        p = p - 1
        if verbose:
            print(indentStr+"rounding down to odd number "+str(p))
    if verbose:
        print(indentStr+"now trying odd numbers in order:")
    ans = 1
    while ans != 0:
        ans = n % p
        if verbose:
            print(indentStr+indentStr+"mod("+str(n)+","+str(p)+")="+str(ans))
        if ans == 0:
            if verbose:
                print("Found p: " + str(p))
            break
        p = p + 2
    q = math.floor(n/p)
    if verbose:
        print("q=floor("+str(n)+"/"+str(p)+")=" + str(q))
    return (p,q)

registerFunction("rsa_pq", {
    "name" : "Find P and Q for RSA",
    "arguments_short":["n","verbose=False"],
    "arguments":["product n=pq of RSA","print commands"],
    "description":"Returns (p,q) where n = pq for RSA"
})