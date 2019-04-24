#inputs
pairs=[
        ["K","H"],
        ["P","X"],
        ["N","K"],
        ["H","R"],
        ["T","F"],
        ["V","Y"],
        ["E","H"],
        ["F","A"],
        ["T","W"],
        ["J","D"],
        ["U","J"]
]
field=3
poly=[1,2,0,1]
alphabet=alphabet

elg_a=11

#code below

letterFields={}
letterPoly=[0,0,0,0]
letterField={}
for i in range(len(alphabet)):
    letterPoly[len(letterPoly)-1]+=1
    for j in range(len(letterPoly)-1,0,-1):
        while letterPoly[j]>=field:
            letterPoly[j]-=field
            letterPoly[j-1]+=1
    letterField[alphabet[i]]=letterPoly.copy()
fields=field_gen(poly,field)
fieldsMod={}

def LUT(ar,val):
    for k,v in ar.items():
        if v==val:
            return k

for k in fields.keys():
    fieldsMod[k%26]=fields[k]

outStr=""
for pair in pairs:
    y1=pair[0].lower()
    y2=pair[1].lower()
    degree1=LUT(fieldsMod,letterField[y1])
    degree2=LUT(fieldsMod,letterField[y2])
    decryptDeg=mod(degree2+(len(alphabet)-degree1*elg_a),len(alphabet))
    outStr=outStr+LUT(letterField,fieldsMod[decryptDeg])
print(outStr)
