def LUT(ar,val):
    if type(ar)==list:
        arLen=len(ar)
        for i in range(arLen):
            if ar[i]==val:
                return i
        return
    for k,v in ar.items():
        if v==val:
            return k

