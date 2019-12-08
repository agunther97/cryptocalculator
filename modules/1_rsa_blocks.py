import math

def rsa_block(n,data):
    blockSize = math.floor(math.log(n,2))
    binaryStr = ("{0:b}".format(data))
    binaryStr.rjust(math.ceil(len(binaryStr)/blockSize)*blockSize)
    parts = [ int(binaryStr[i:i+blockSize],2) for i in range(0, len(binaryStr), blockSize)]
    
    return parts