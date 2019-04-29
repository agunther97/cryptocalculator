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

def eulerCriterion(a,p):
    if (a%p==0):
        return 0
    val=pow(a,int((p-1)/2),p)
    if (val==1):
        return 1
    if (val==0):
        return 0
    if (val==p-1):
        return -1

def jacobi(x,n):
    factors = jc_factors(n)
    factorsCondensed={}
    for fac in factors:
        if fac in factorsCondensed:
            factorsCondensed[fac]+=1
        else:
            factorsCondensed[fac]=1
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
        out+="("+str(xmod)+"/"+str(fac)+")"
        if (exp>1):
            out+=superscript(exp)
        out+="*"
        crit=eulerCriterion(xmod,fac)
        outPt2+="("+str(crit)+")"
        if (exp>1):
            outPt2+=superscript(exp)
        outPt2+="*"
        if (xmod!=0):
            res*=pow(crit,exp)
    out=out[:-1]
    outPt2=outPt2[:-1]
    out+="="+outPt2
    out+="="+str(res)
    print(out)
    return res
