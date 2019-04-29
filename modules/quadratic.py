def jc_factors(nr):
    i = 2
    factors = []
    while i <= nr:
        if (nr % i) == 0:
            factors.append(i)
            nr = nr / i
        else:
            i = i + 1
    return factors

def eulerCriterion(a,p,verbose=False):
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
    factors = jc_factors(n)
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
    out=str(x)+"/"+str(n)+"="
    outPt2=""
    for fac in factorsCondensed.keys():
        xmod=x%fac
        exp=factorsCondensed[fac]
        crit=eulerCriterion(xmod,fac)
        if verbose:
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
        print(out)
        for fac in factorsCondensed.keys():
            xmod=x%fac
            exp=factorsCondensed[fac]
            crit=eulerCriterion(xmod,fac,True)
        if composite:
            outPt2+="="+str(res)
            print(outPt2)
    return res
