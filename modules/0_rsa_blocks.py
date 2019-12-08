import math

registerFunction("rsa_block", {
    "name" : "Number to RSA Blocks",
    "arguments_short":["n","data","verbose=False"],
    "arguments":["n=p*q","large number","print steps"],
    "description":"Converts large number to array of blocks below N"
})

def rsa_block(n,data,verbose=False):
    blockSize = math.floor(math.log(n,2))
    if verbose:
        print("Block size: " + str(blockSize))
    binaryStr = ("{0:b}".format(data))
    if verbose:
        print("Binary string: ")
        print(binaryStr)
    binaryStr.rjust(math.ceil(len(binaryStr)/blockSize)*blockSize,"0")
    if verbose:
        print("Padded binary string: ")
        print(binaryStr)
    if verbose:
        print("Array of binary strings: ")
        print([ binaryStr[i:i+blockSize] for i in range(0, len(binaryStr), blockSize)])
    parts = [ int(binaryStr[i:i+blockSize],2) for i in range(0, len(binaryStr), blockSize)]
    if verbose:
        print("Array of ints: ")
        print(parts)
    
    return parts

registerFunction("rsa_unblock", {
    "name" : "RSA Blocks to Number",
    "arguments_short":["n","data","verbose=False"],
    "arguments":["n=p*q","blocks","print steps"],
    "description":"Converts array of rsa blocks to number. Pair with hex(x) for formatting."
})

def rsa_unblock(n,data,verbose=False):
    blockSize = math.floor(math.log(n,2))
    if verbose:
        print("Block size: " + str(blockSize))
    binaryStr=""
    if verbose:
        print("Blocks:")
    for x in data:
        if verbose:
            print(("{0:b}".format(x)).rjust(blockSize,"0"))
        binaryStr +=("{0:b}".format(x)).rjust(blockSize,"0")
    if verbose:
        print("Binary string: " + binaryStr)
    num = int(binaryStr,2)
    if verbose:
        print("Int value: " + str(num))
        print("Hex value: " + hex(num))
    return num