def primitive_roots(modulo,verbose=False):
    if is_prime(modulo):
        n=modulo
        nsub=n-1
        factors=factor(nsub)
        if verbose:
            print("Factors: "+str(factors))
            print("Raising each number to factors until prim root is found.")
        primRoot=-1
        for i in range(1,n):
            isPrim=True
            s=""
            for fac in factors:
                p=pow(i,fac,n)
                s+=str(i)+superscript(fac)+" mod "+str(n)+"="+str(p)+", "
                if fac!=nsub and p==1:
                    s=s[:-2]+" - not prime.  "
                    isPrim=False
                    break
            s=s[:-2]
            if verbose:
                print(s)
            if isPrim:
                if verbose:
                    print("Primitive root found!")
                primRoot=i
                break
        if primRoot == -1:
            if verbose:
                print("No primitive roots!")
            return
        else:
            coprime_set = {num for num in range(1, nsub) if gcd(num, nsub) == 1}
            if verbose:
                print("Raising "+str(primRoot)+" to coprimes n-1: ")
                print(coprime_set)
            roots=[]
            for ex in coprime_set:
                p=pow(primRoot,ex,n)
                roots.append(p)
                if verbose:
                    print(str(primRoot)+superscript(ex)+" mod "+str(n)+"="+str(p))
            return sorted(roots)
        return
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

registerFunction("primitive_elements", {
"name" : "Find Primitive Elements",
"arguments_short":["mod","verbose=False"],
"arguments":["mod value", "give step-by-step instructions"],
"description":"Returns all primitive elements under a mod"})