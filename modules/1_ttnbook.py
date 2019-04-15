def nttbook(data,alpha=alphabet,segLen=3):
    if type(data) is int:
        data = [data]
    output=""
    for n in data:
        segOutput=""
        z=len(alpha)
        #don't log it, instead just use 3 as this is how the book encodes
        try:
            varPow = math.floor(math.log(n,z)) #biggest power
        except:
            varPow = 0
        if not (segLen is None):
            varPow = segLen-1
        while (varPow>=0):
            div = pow(z,varPow)
            char=alpha[math.floor(n/div+0.001)]
            n=n%div
            varPow-=1
            segOutput+=char
        output+=segOutput
    return output
