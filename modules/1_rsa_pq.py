import math,random

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

#Algorithm 5.10
def rsa_pq_vegas(n,e,d,attempts=100,verbose=False):
    s=0
    r=(e*d-1)
    while r%2==0:
        r=r>>1
        s+=1
    r=int(r)
    if verbose:
        print("s="+str(s))
        print("ab-1=2"+superscript(s)+"*"+str(r))
    for i in range(attempts):
        w=1+int(randrange(0,n-1))
        x=gcd(w,n)
        if 1<x and x<n:
            return x #x is a factor of n
        v=pow(w,r,n)
        if (v==1):
            continue
        v0=v
        while (v!=1):
            v0=v
            v=pow(v,2,n)
            #print(v)
        if (v0==n-1):
            continue
        else:
            x=gcd(v0+1,n)
            if verbose:
                print("Success @ Attempt #"+str(i+1))
            return x

registerFunction("rsa_pq", {
    "name" : "Find P and Q for RSA",
    "arguments_short":["n","verbose=False"],
    "arguments":["product n=pq of RSA","print commands"],
    "description":"Returns (p,q) where n = pq for RSA"
})