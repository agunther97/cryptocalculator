def ntt_book(data,alpha=alphabet,segLen=3):
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

registerFunction("ntt_book", {
    "name" : "Numbers to text (Book)",
    "arguments_short":["data","alpha=alphabet","segLen=3"],
    "arguments":["data to convert","alphabet=list like [\"a\",\"b\",...]","segLen=letters per number"],
    "description":"Converts numbers to text using the book algorithm"
})