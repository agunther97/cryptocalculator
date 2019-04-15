import math

def multiplicative_inverse(a,p):
    a_0 = p
    b_0 = a
    t_0 = 0
    t = 1
    q = math.floor(a_0/b_0)
    r = a_0 - (q * b_0)
    while r > 0:
        temp = (t_0 - (q * t)) % p
        t_0 = t
        t = temp
        a_0 = b_0
        b_0 = r
        q = math.floor(a_0/b_0)
        r = a_0 - (q * b_0)
    return t

def inv(a,p):
    return multiplicative_inverse(a,p)

registerFunction("multiplicative_inverse", {
    "name" : "Find multiplicative inverse",
    "arguments_short":["x", "y"],
    "arguments":["value", "mod"],
    "description":"Returns x^-1 mod y"
})

registerFunction("inv", {
    "name" : "Find multiplicative inverse",
    "arguments_short":["x", "y"],
    "arguments":["value", "mod"],
    "description":"Returns x^-1 mod y"
})