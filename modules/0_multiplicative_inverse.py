import math

def multiplicative_inverse(a,b):
    a_0 = a
    b_0 = b
    t_0 = 0
    t = 1
    q = math.floor(a_0/b_0)
    r = a_0 - (q * b_0)
    while r > 0:
        temp = (t_0 - (q * t)) % a
        t_0 = t
        t = temp
        a_0 = b_0
        b_0 = r
        q = math.floor(a_0/b_0)
        r = a_0 - (q * b_0)
    return t

def inv(a,b):
    return multiplicative_inverse(a,b)

registerFunction("multiplicative_inverse", {
    "name" : "Find multiplicative inverse",
    "arguments_short":["a", "b"],
    "arguments":["mod", "value"],
    "description":"Returns b^-1 mod a"
})