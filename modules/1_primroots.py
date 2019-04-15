def primitive_roots(modulo):
    coprime_set = {num for num in range(1, modulo) if gcd(num, modulo) == 1}
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