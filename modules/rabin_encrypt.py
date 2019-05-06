def rabin_encrypt(x,p,q,verbose=False):
    if p % 4 != 3:
        return 'p must = 3 in mod 4'
    elif q % 4 != 3:
        return 'q must = 3 in mod 4'
    n = p*q
    y = pow(x,2,n)
    if verbose:
        print('y = ' + str(y))
    return y

registerFunction("rabin_encrypt", {
"name" : "Encrypt Rabin Cryptosystem",
"arguments_short":["x","p", "q", "verbose=False"],
"arguments":["x=plaintext as numbers", "p=prime s.t. p = 3 mod 4", "q=prime s.t. q = 3 mod 4", "give step-by-step instructions"],
"description":"Returns encrypted ciphertext"})