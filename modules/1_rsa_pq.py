import math

def rsa_pq(n):
    p = math.floor(math.sqrt(n))
    if p % 2 == 0:
        p = p - 1
    ans = 1
    while ans != 0:
        ans = n % p
        if ans == 0:
            break
        p = p + 2
    q = math.floor(n/p)
    return (p,q)

registerFunction("rsa_pq", {
    "name" : "Find P and Q for RSA",
    "arguments_short":["n"],
    "arguments":["large public prime n of RSA"],
    "description":"Returns (p,q) where n = pq for RSA"
})