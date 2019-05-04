def vigenere_encrypt(s,k,alphabet=alphabet,verbose=False):
    modulo=len(alphabet)
    numberString=[None]*len(s)
    sLen=len(s)
    kLen=len(k)
    if type(s)==list:
        for i in range(sLen):
            numberString[i]=s[i]
    else:
        for i in range(sLen):
            numberString[i]=LUT(alphabet,s[i])
    if verbose:
        print("String Numbers:")
        print(numberString)
    numberKeyString=[None]*kLen
    if type(k)==list:
        for i in range(kLen):
            numberKeyString[i]=k[i]
    else:
        for i in range(kLen):
            numberKeyString[i]=LUT(alphabet,k[i])
    if verbose:
        print("Key Numbers:")
        print(numberKeyString)
    out=[None]*sLen
    for i in range(sLen):
        out[i]=(numberString[i]+numberKeyString[i%kLen])%modulo
        if verbose:
            print("x"+subscript(i+1)+"=s"+subscript(i+1)+"+k"+subscript((i%kLen)+1)+"="+str(numberString[i])+"+"+str(numberKeyString[i%kLen])+" mod " + str(modulo)+"="+str(out[i]))
    if verbose:
        print("Output Numbers:")
        print(out)
    outStr=""
    for i in range(sLen):
        outStr+=alphabet[out[i]]
    return outStr

def vigenere_decrypt(s,k,alphabet=alphabet,verbose=False):
    modulo=len(alphabet)
    numberString=[None]*len(s)
    sLen=len(s)
    kLen=len(k)
    if type(s)==list:
        for i in range(sLen):
            numberString[i]=s[i]
    else:
        for i in range(sLen):
            numberString[i]=LUT(alphabet,s[i])
    if verbose:
        print("String Numbers:")
        print(numberString)
    numberKeyString=[None]*kLen
    if type(k)==list:
        for i in range(kLen):
            numberKeyString[i]=k[i]
    else:
        for i in range(kLen):
            numberKeyString[i]=LUT(alphabet,k[i])
    if verbose:
        print("Key Numbers:")
        print(numberKeyString)
    out=[None]*sLen
    for i in range(sLen):
        out[i]=(numberString[i]-numberKeyString[i%kLen])%modulo
        if verbose:
            print("x"+subscript(i+1)+"=s"+subscript(i+1)+"-k"+subscript((i%kLen)+1)+"="+str(numberString[i])+"-"+str(numberKeyString[i%kLen])+" mod " + str(modulo)+"="+str(out[i]))
    if verbose:
        print("Output Numbers:")
        print(out)
    outStr=""
    for i in range(sLen):
        outStr+=alphabet[out[i]]
    return outStr

def check_shifted(s,shift):
    for i in range(shift,len(s)-shift):
        if s[i]!=s[i-shift]:
            return False
    return True

def vigenere_key(p,c,alphabet=alphabet,verbose=False):
    modulo=len(alphabet)
    sLen=len(p)
    pString=[None]*sLen
    cString=[None]*sLen
    kString=[None]*sLen
    if type(p)==list:
        for i in range(sLen):
            pString[i]=p[i]
    else:
        for i in range(sLen):
            pString[i]=LUT(alphabet,p[i])
    if type(c)==list:
        for i in range(sLen):
            cString[i]=c[i]
    else:
        for i in range(sLen):
            cString[i]=LUT(alphabet,c[i])
    for i in range(sLen):
        kString[i]=(cString[i]-pString[i])%modulo
    if verbose:
        print("P String:")
        print(pString)
        print("C String:")
        print(cString)
        print("K String:")
        print(kString)
    keyLen=sLen
    for i in range(1,len(kString)+1):
        if check_shifted(kString,i):
            keyLen=i
            break
    keyAr=kString[0:keyLen]
    if verbose:
        print("Key Length:")
        print(keyLen)
    outStr=""
    for i in range(keyLen):
        outStr+=alphabet[keyAr[i]]
    return outStr
