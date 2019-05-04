def split2len(x, n):
    chunks, chunk_size = len(x), n
    return [ x[i:i+chunk_size] for i in range(0, chunks, chunk_size) ]

def euler_criterion(a,p,verbose=False):
    ret = None
    if (a%p==0):
        ret = 0
    val=pow(a,int((p-1)/2),p)
    if (val==1):
        ret = 1
    if (val==0):
        ret = 0
    if (val==p-1):
        ret = -1
    if verbose:
        print(str(a)+"/"+str(p)+"="+str(a)+"^(("+str(p)+"-1)/2)="+str(ret))
    return ret

def jacobi(x,n,verbose=False):
    #currently uses euler criterion, so only works on certain composites. Needs alternate method?
    factors = factor_prime(n)
    factorsCondensed={}
    for fac in factors:
        if fac in factorsCondensed:
            factorsCondensed[fac]+=1
        else:
            factorsCondensed[fac]=1
    composite=(len(factors)>1 or (len(factors)==1 and factorsCondensed[factors[0]]>1))
    if verbose and composite:
        print("factors:")
        print(factorsCondensed)
    if x%n==0:
        return 0
    res=1
    out=""
    if composite:
        out=str(x)+"/"+str(n)+"="
    outPt2=""
    for fac in factorsCondensed.keys():
        xmod=x%fac
        exp=factorsCondensed[fac]
        crit=euler_criterion(xmod,fac)
        if verbose and composite:
            out+="("+str(xmod)+"/"+str(fac)+")"
            outPt2+="("+str(crit)+")"
            if (exp>1):
                out+=superscript(exp)
                outPt2+=superscript(exp)
            out+="*"
            outPt2+="*"
        if (xmod!=0):
            res*=pow(crit,exp)
    if verbose:
        out=out[:-1]
        outPt2=outPt2[:-1]
        if len(out.strip())>0:
            print(out)
        for fac in factorsCondensed.keys():
            xmod=x%fac
            exp=factorsCondensed[fac]
            crit=euler_criterion(xmod,fac,True)
        if composite:
            outPt2+="="+str(res)
            print(outPt2)
    return res

def quadratic_residues(x,verbose=False):
    delim="|"
    if is_prime(x) and x>30:
        residues={}
        for i in range(x):
            n=i+1
            jac=jacobi(n,x,verbose)
            residues[n]=False
            if (jac>0):
                residues[n]=True
        residueList=[]
        ln=1
        for k in residues.keys():
            ln=max(ln,len(str(k)))
            ln=max(ln,len(str(residues[k])))
        s=""
        s2=""
        for k in sorted(residues.keys()):
            v=residues[k]
            s+=tintTrueFalse(str(k).ljust(ln),v)+delim
            s2+=tintTrueFalse(str(residues[k]).ljust(ln),v)+delim
            if v:
                residueList.append(k)
        if verbose:
            sChunks=split2len(s,160)
            sChunks2=split2len(s2,160)
            for i in range(len(sChunks)):
                fChar=sChunks[i][0]
                if fChar and (not fChar.isalpha()) and (not fChar.isnumeric()) and (fChar!="|"):
                    sChunks2[i]=fChar+sChunks2[i]
                print(sChunks[i])
                #if lastChar and (not lastChar.isalpha()) and (not lastChar.isnumeric()):
                    #sChunks2[i]+=lastChar.replace("\n","")
                print(sChunks2[i])
                lastChar=s[-1]
        return residueList
    else:
        if verbose:
            print("Generating table of squares.")
            tab={}
            residueList=[]
            for i in range(1,x):
                tab[i]=pow(i,2,x)
                if not (tab[i] in residueList):
                    residueList.append(tab[i])
            ln=1
            for k in tab.keys():
                ln=max(ln,len(str(k)))
                ln=max(ln,len(str(tab[k])))
            if verbose:
                s=""
                s2=""
                for k in sorted(tab.keys()):
                    s+=str(k).ljust(ln)+delim
                    s2+=str(tab[k]).ljust(ln)+delim
                print("x:  "+s)
                print("x"+superscript(2)+": "+s2)
            if 0 in residueList:
                residueList.remove(0)
            return sorted(residueList)
                
registerFunction("quadratic_residues", {
    "name" : "Quadratic Residues",
    "arguments_short":["modulo","verbose=False"],
    "arguments":["modulo","print commands"],
    "description":"Returns quadratic residues of a modulo"
})

registerFunction("euler_criterion", {
    "name" : "Euler's Criterion",
    "arguments_short":["x","p","verbose=False"],
    "arguments":["number","modulo (prime)","print commands"],
    "description":"Returns if number is a quadratic residue of a prime"
})