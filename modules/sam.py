import math

def sam(x, c, n):
    c = int(c)
    c = '{0:b}'.format(c) #to binary
    z = 1
    l = len(c)
    for i in range(l):
        z = (math.pow(z, 2)) % n
        if(c[i] == "1"):
            z = (z*x) % n
    return z

registerFunction("sam", {
    "name" : "Square and Multiply",
    "arguments_short":["x", "c", "n"],
    "arguments":["base", "exponent", "mod"],
    "description":"Returns a float z s.t. x^c mod n = z"
})