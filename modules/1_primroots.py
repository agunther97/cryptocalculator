def primitive_roots(modulo,verbose=False):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
    if verbose:
        print("coprimes:")
        isList=True
        for num in range(1,modulo):
            if gcd(num,modulo)!=1:
                isList=False
        if isList:
            print(str(1)+"->"+str(modulo-1))
        else:
            print(coprime_set)
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]

def is_primitive_root(n,mod):
    cache = {}
    for i in range(1,mod,1):
        x=pow(n,i,mod)
        if x in cache:
            return False
        else:
            cache[x]=i
    return True

def primitive_elements(mod,verbose=False):
    return primitive_roots(mod,verbose)