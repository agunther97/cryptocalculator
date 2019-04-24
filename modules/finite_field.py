#format:
#poly=[coeff_0,coeff_x,coeff_x2,...]
def modAr(ar,field):
    for i in range(len(ar)):
        ar[i]=mod(ar[i],field)
def addAr(ar1,ar2):
    for i in range(len(ar1)):
        ar1[i]=ar1[i]+ar2[i]
def dispAr(ar):
    s=""
    for i in range(len(ar)):
        if (ar[i]!=0):
            if i==len(ar)-1:
                s+=str(ar[i])+" "
            else:
                s+=str(ar[i])+"x^"+str(len(ar)-i-1)+"+"
    print(s[:-1])
def field_gen(poly,field):
    print("input:")
    dispAr(poly)
    degree=len(poly)-1
    powers={}
    subpoly=[None]*(degree+1)
    for i in range(degree+1):
        subpoly[i]=mod(field-poly[i],field)
    subpoly[0]=0
    powers[degree]=subpoly
    tmppoly=subpoly.copy()
    index=degree
    while True:
        for i in range(len(tmppoly)-1):
            tmppoly[i]=tmppoly[i+1]
        tmppoly[len(tmppoly)-1]=0
        for j in range(tmppoly[0]):
            tmppoly[0]-=1
            addAr(tmppoly,subpoly)
            modAr(tmppoly,field)
        index+=1
        powers[index]=tmppoly.copy()
        bk=False
        for k,v in powers.items():
            if k==index:
                continue
            eq=True
            for x in range(len(v)):
                if v[x]!=tmppoly[x]:
                    eq=False
            if eq:
                bk=True
                break
        if bk:
            break
    return powers
