def genTable(fieldSize,depth):
    ret=[]
    for i in range(fieldSize):
        l=[[]]
        if depth>0:
            l=genTable(fieldSize,depth-1)
        for li in l:
            li.append(i)
            ret.append(li)
    return ret

def multiply_polynomial(poly1,poly2,modu=None):
    poly={}
    for i in range(len(poly1)):
        degree1=len(poly1)-i-1
        for j in range(len(poly2)):
            degree2=len(poly2)-j-1
            degProduct=degree1+degree2
            product=poly1[i]*poly2[j]
            if not (degProduct in poly):
                poly[degProduct]=0
            poly[degProduct]+=product
    highKey=0
    for k in poly.keys():
        highKey=max(highKey,k+1)
    polyList=[0]*highKey
    for k,v in poly.items():
        key=highKey-k-1
        if not (modu is None):
            polyList[key]=mod(v,modu)
        else:
            polyList[key]=v
    while len(polyList)>0 and polyList[0]==0:
        polyList.pop(0)
    return polyList
def degree_polynomial(poly):
    tmp=poly.copy()
    while len(tmp)>0 and tmp[0]==0:
        tmp.pop(0)
    return len(tmp)-1

def factor_polynomial(poly,field,verbose=False):
    degree=len(poly)-1
    attempts={}
    tabl=genTable(field,ceil((degree+2)/2))
    for i in range(len(tabl)):
        for j in range(len(tabl)):
            if i in attempts:
                if j in attempts[i]:
                    continue
                else:
                    attempts[i][j]=True
            else:
                attempts[i]={}
            if j in attempts:
                if i in attempts[j]:
                    continue
            p1=tabl[i]
            p2=tabl[j]
            if degree_polynomial(p1)+degree_polynomial(p2)==degree_polynomial(poly):
                mul=multiply_polynomial(p1,p2,field)
                eq=(mul==poly)
                if verbose:
                    s="("+format_polynomial(p1)+")*("+format_polynomial(p2)+")"
                    if not eq:
                        s=strike(s)
                    s=tintTrueFalse(s,eq)
                    print(s)
                if mul==poly:
                    return [p1,p2]

def format_polynomial(poly):
    if (poly is None) or (poly[0] is None):
        return ("None")
    if type(poly[0])!=list:
        poly=[poly]
    out=""
    for ar in poly:
        s=""
        for i in range(len(ar)):
            if (ar[i]!=0):
                if i==len(ar)-1:
                    s+=str(ar[i])+" "
                else:
                    if ar[i]==1:
                        s+="x^"+str(len(ar)-i-1)+"+"
                    else:
                        s+=str(ar[i])+"x^"+str(len(ar)-i-1)+"+"
        out+=(s[:-1])+"\n"
    return out[:-1]
