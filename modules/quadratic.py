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
    factors = factor_primitive(n)
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
    residues={}
    delim="|"
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
        print(s)
        print(s2)
    return residueList