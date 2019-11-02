#markdown documentation
def doc_md():
    sz=len(calculatorFunctions.keys())
    funcList = [None for x in range(sz)]
    i=0
    for k,v in calculatorFunctions.items():
        funcList[i]=k
        i+=1
    funcList.sort()
    i=0
    s=""
    for fn in funcList:
        data=calculatorFunctions[fn]

        if "name" in data:
            print(tcolors.HEADER+data["name"]+tcolors.ENDC)
        else:
            print(tcolors.HEADER+fn+tcolors.ENDC)
        args = []
        if "arguments" in data:
            args=data["arguments"]
        elif "arguments_short" in data:
            args=data["arguments_short"]
        s="Usage: " + fn + "("
        for j in range(len(args)):
            s=s+args[j]
            if j<len(args)-1:
                s=s+", "
        s=s+")"
        fmtWrite(indentStr+s," ",indent=(indentStr+indentStr))
        if "description" in data:
            fmtWrite(indentStr+data["description"], " ",indent=(indentStr+indentStr))