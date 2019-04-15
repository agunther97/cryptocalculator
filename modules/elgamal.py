def elgamal_encrypt(x,p,alpha,a):
    return elgamale(x,p,alpha,pow(alpha,a,p))

def elgamale(x,p,alpha,beta):
    lx=x
    if type(x)==int:
        lx=[x]
    d=len(lx)
    w=[[0 for x in range(d)] for y in range(2)] 
    for j in range(0,d,1):
        k=rand(p-1)
        w[0][j]=pow(alpha,k,p)
        w[1][j]=mod(lx[j]*pow(beta,k,p),p)
    return w

def elgamald(y,p,a):
    t=[]
    d=len(y[1])
    for j in range(0,d,1):
        y1=y[0][j]
        y2=y[1][j]
        s=mod(y2*inv(pow(y1,a,p),p),p)
        t.append(s)
    return t