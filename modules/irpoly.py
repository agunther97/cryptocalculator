import itertools

def formatPolynomial(poly):
    s=""
    l=len(poly)
    for i in range(l-1):
        #if (poly[i]!=0):
            #if (poly[i]==1):
            #    s=s+"x^"+str(l-1-i)+"+"
            #else:
        s=s+str(poly[i])+"x^"+str(l-1-i)+"+"
    #if (poly[l-1]!=0):
    s=s+str(poly[l-1])
    return s

def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result

def irreducible_poly_verbose(degree, field_size, fast=True, quiet=False):
    degRange = range(degree)
    degRangeAdd = range(degree+1)
    fieldRange = range(field_size)

    results = {}
    resultsTable = [{} for i in range(field_size)]
    product_list = [i for i in range(field_size)]
    product_list_f = product_list.copy()
    product_list_f.pop(0)
    entries = [None]*(degree+1)
    if fast:
        entries[0] = [1]
    else:
        entries[0] = product_list_f#.copy()
    for i in degRange:
        entries[i+1] = product_list
    polys=list(itertools.product(*entries))
    for poly in polys:
        results[poly]=True
        for x in fieldRange:
            total=0
            for i in degRangeAdd:
                total+=(pow(x,degree-i)*poly[i])
            if (total%field_size)==0:
                results[poly]=False
                break
    resKeys = results.keys()
    for i in degRange:
        resKeys = sorted(resKeys, key=lambda poly:poly[i])
    
    count=0
    s=""
    for i in range(len(resKeys)):
        k=resKeys[i]
        v=results[k]
        app=formatPolynomial(k)
        if not v:
            app=strike(app)
        s=s+app+"\t"
        if (i+1)%field_size==0:
            s=s[:-1]
            if not quiet:
                print(s)
            s=""

        if v:
            count+=1
    if fast:
        count=count*(field_size-1)
    return count
