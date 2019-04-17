def elgamal_alpha(p,verbose=False):
    if verbose:
        print("Generating alpha for " + str(p))
    for i in range(1,p):
        if verbose:
            print("Checking value "+str(i))
        if is_primitive_root(i,p):
            if verbose:
                print("Found primitive: " + str(i))
            return i
    return -1

def elgamal_beta(p,alpha,a,verbose=False):
    if verbose:
        print("beta=sam(alpha,a,p)=sam("+str(alpha)+","+str(a)+","+str(p)+")="+str(pow(alpha,a,p)))
    return pow(alpha,a,p)

def elgamal_encrypt(x,p,alpha,a,k=None,verbose=False):
    return elgamale(x,p,alpha,elgamal_beta(p,alpha,a,verbose=verbose),k=k,verbose=verbose)

def elgamal_decrypt(y,p,a,verbose=False):
    return elgamald(y,p,a,verbose=verbose)

def elgamal_k(p,a,verbose=True):
    if verbose:
        print("minimum effective k is ceil(ln(p)/ln(a))=ceil("+str(ln(p))+"/"+str(ln(a))+")="+str(ceil(ln(p)/ln(a))))
    return ceil(ln(p)/ln(a))

def elgamale(x,p,alpha,beta,k=None,verbose=False):
    lx=x
    if type(x)==int:
        lx=[x]
    d=len(lx)
    w=[[0 for x in range(d)] for y in range(2)] 
    for j in range(0,d,1):
        resetK=False
        if (k is None):
            k=rand(p-1)
            resetK=True
        w[0][j]=pow(alpha,k,p)
        w[1][j]=mod(lx[j]*pow(beta,k,p),p)
        if verbose:
            if j==0 and d==1:
                print(indentStr+"y"+subscript(1)+"=sam(alpha,k,p)=sam("+str(alpha)+","+str(k)+","+str(p)+")=" + str(w[0][j]))
                print(indentStr+"y"+subscript(2)+"=x*sam(beta,k,p)=mod("+str(lx[j])+"*sam("+str(beta)+","+str(k)+","+str(p)+"),"+str(p)+")=" + str(w[1][j]))
            else:
                subs=subscript(j+1)
                print(indentStr+"y1"+subs+"=sam(alpha,k,p)=sam("+str(alpha)+","+str(k)+","+str(p)+")=" + str(w[0][j]))
                print(indentStr+"y2"+subs+"=x*sam(beta,k,p)=mod("+str(lx[j])+"*sam("+str(beta)+","+str(k)+","+str(p)+"),"+str(p)+")=" + str(w[1][j]))
        if resetK:
            k=None
    return w

def elgamald(y,p,a,verbose=False):
    t=[]
    d=len(y[1])
    for j in range(0,d,1):
        y1=y[0][j]
        y2=y[1][j]
        if verbose:
            print("x"+subscript(j+1)+"=mod(y2"+subscript(j+1)+"*inv(sam(y1"+subscript(j+1)+",a,p),p),p)=mod("+str(y2)+"*inv(sam("+str(y1)+","+str(a)+","+str(p)+"),"+str(p)+"),"+str(p)+")")
        s=mod(y2*inv(pow(y1,a,p),p),p)
        t.append(s)
    return t

registerFunction("elgamal_alpha", {
    "name" : "Elgamal Generate Alpha",
    "arguments_short":["p","verbose=False"],
    "arguments":["modulous","print commands"],
    "description":"Computes first primitive root of a prime"
})

registerFunction("elgamal_beta", {
    "name" : "Elgamal Generate Alpha",
    "arguments_short":["p","alpha","a","verbose=False"],
    "arguments":["modulous","alpha","secret","print commands"],
    "description":"Computes beta for Elgamal given modulo, alpha, and a"
})

registerFunction("elgamale", {
    "name" : "Elgamal Encryption",
    "arguments_short":["data","p","alpha","a","k=None","verbose=False"],
    "arguments":["plaintext number list","modulous","alpha","beta","random value","print commands"],
    "description":"Computes ciphertext using Elgamal encryption"
})

registerFunction("elgamal_encrypt", {
    "name" : "Elgamal Encryption",
    "arguments_short":["data","p","alpha","a","k=None","verbose=False"],
    "arguments":["plaintext number list","modulous","alpha","secret value","random value","print commands"],
    "description":"Computes ciphertext using Elgamal encryption"
})

registerFunction("elgamald", {
    "name" : "Elgamal Decryption",
    "arguments_short":["data","p","a"],
    "arguments":["ciphertext number list","modulous","a"],
    "description":"Computes plaintext using Elgamal decryption"
})

registerFunction("elgamal_decrypt", {
    "name" : "Elgamal Decryption",
    "arguments_short":["data","p","a"],
    "arguments":["ciphertext number list","modulous","a"],
    "description":"Computes plaintext using Elgamal decryption"
})