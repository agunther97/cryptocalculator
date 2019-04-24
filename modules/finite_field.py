#format:
#poly=[coeff_0,coeff_x,coeff_x2,...]
def modAr(ar,field):
    for i in range(len(ar)):
        ar[i]=mod(ar[i],field)
def addAr(ar1,ar2):
    for i in range(len(ar1)):
        if i in ar2:
            ar1[i]=ar1[i]+ar2[i]
def field_gen(poly,field):
    degree=len(poly)-1
    poly.append(0)
    powers=[]
    tmppoly=poly.copy()
    subpoly=[None]*degree
    for i in range(degree):
        subpoly[i]=field-poly[i]
    print(subpoly)
    while True:
        for i in range(degree+1):
            index=degree-i
            tmppoly[index+1]=tmppoly[index]
            modAr(tmppoly,field)
            for j in range(tmppoly[degree+1]):
                tmppoly[degree+1]-=1
                addAr(subpoly,tmppoly)
                modAr(tmppoly,field)
        print(tmppoly)
        break
    return powers
