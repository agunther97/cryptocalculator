import math

def ntt_book(data,segLen=3,alpha=alphabet):
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

def ttn_book(strv,segLen=3,alpha=alphabet):
    invAlpha = {}
    for i in range(len(alpha)):
        invAlpha[alpha[i]]=i
    inputs = [strv[i:i+segLen] for i in range(0, len(strv), segLen)]
    out = [None]*len(inputs)
    for i in range(len(inputs)):
        s=inputs[i]
        while (len(s)<segLen):
            s=s+"z"
        inputs[i]=s
        out[i]=0
        for j in range(segLen):
            ch=s[j]
            if ch in invAlpha:
                out[i]+=invAlpha[ch]*pow(len(alpha),segLen-j-1)
    return out

registerFunction("ntt_book", {
    "name" : "Numbers to text (Book)",
    "arguments_short":["data","segLen=3","alpha=alphabet"],
    "arguments":["data to convert","segLen=letters per number","alphabet=list like [\"a\",\"b\",...]"],
    "description":"Converts numbers to text using the book algorithm"
})

registerFunction("ttn_book", {
    "name" : "Text to numbers (Book)",
    "arguments_short":["data","segLen=3","alpha=alphabet"],
    "arguments":["data to convert","segLen=letters per number","alphabet=list like [\"a\",\"b\",...]"],
    "description":"Converts text to numbers using the book algorithm"
})