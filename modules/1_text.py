def ttn(txt,m):
    txt=lower(txt)
    n=len(txt)
    ntxt=[]
    r=mod(n,m)
    q=floor(n/m)
    for i in range(0,q-1,1):
        k=0
        for j in range(1,m,1):
            t=txt[m*i+j]
            if t==" ":
                k=28*k+27
            else:
                k=28*k+ord(t)-96
        ntxt.append(k)
    if (n-m*q)>0:
        k=0
        for j in range(1,r,1):
            t=txt[m*q+j]
            if t==" ":
                k=28*k+27
            else:
                k=28*k+ord(t)-96
        ntxt.append(k)
    if len(ntxt)==1:
        return ntxt[1]
    else:
        return ntxt