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