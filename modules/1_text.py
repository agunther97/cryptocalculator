def ttn(txt,m):
    txt=lower(txt)
    n=len(txt)
    ntxt=[]
    r=mod(n,m)
    q=floor(n/m)
    for i in range(0,q,1):
        k=0
        for j in range(0,m,1):
            t=txt[m*i+j]
            if t==" ":
                k=28*k+27
            else:
                k=28*k+ord(t)-96
        ntxt.append(k)
    if (n-m*q)>0:
        k=0
        for j in range(0,r,1):
            t=txt[m*q+j]
            if t==" ":
                k=28*k+27
            else:
                k=28*k+ord(t)-96
        ntxt.append(k)
    if len(ntxt)==1:
        return ntxt[0]
    else:
        return ntxt
def ntt(lst):
    t=""
    if type(lst)==int:
        lst=[lst]
    for i in range(len(lst)):
        bt=""
        n=lst[i]
        while n>0:
            c=int(mod(n,28))
            if c==27:
                bt=" "+bt
            else:
                bt=chr(c+96)+bt
            n=(n-c)/28
        t=t+bt
    return t
    