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

def tintTrueFalse(text, succ):
    if succ:
        text=tcolors.OKGREEN+text
    else:
        text=tcolors.FAIL+text
    text+=tcolors.ENDC
    return text

def irreducible_poly(degree, field_size, fast=True, verbose=False):
    if ((not verbose) and (field_size<=3)):
        return irreducible_poly_lite(degree, field_size)
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
        resKeys = sorted(resKeys, key=lambda poly:poly[i+1])
    resKeys = sorted(resKeys, key=lambda poly:poly[0])

    count=0
    s=""
    for i in range(len(resKeys)):
        k=resKeys[i]
        v=results[k]
        app=formatPolynomial(k)
        if not v:
            app=strike(app)
        app=tintTrueFalse(app,v)
        s=s+app+"\t"
        if (i+1)%field_size==0:
            s=s[:-1]
            if verbose:
                print(s)
            s=""

        if v:
            count+=1
    if fast:
        count=count*(field_size-1)
    return count


def irreducible_poly_lite(degree, field_size):
    polys = [1]
    product_list = [i for i in range(field_size)]
    for i in range(degree):
        polys = list(itertools.product(polys, product_list))
    flat_polys = []
    for entry in polys:
        entry_str = str(entry)
        poly_pieces= []
        for letter in entry_str:
            if str.isdigit(letter):
                poly_pieces.append(int(letter))
        flat_polys.append(poly_pieces)
    reduceable_count = 0
    for poly in flat_polys:
        for i in range(0, field_size):
            if (pow(i,degree) + poly[1]*i + poly[2]) % field_size == 0:
                reduceable_count += 1
                break
    return ((len(polys) - reduceable_count) * (field_size - 1))

registerFunction("irreducible_poly", {
    "name" : "Irreducible Polynomials over Field",
    "arguments_short":["degree","field_size","fast=True","verbose=False"],
    "arguments":["the degree of the polynominal", "the field size (i.e. Z mod #)","use fast algorithm? default on, only calculates leading coeff. 1 and extrapolates", "print formatted table"],
    "description":"Returns the number of irreducible polynomials for a given field size"
})
