polies=[
        [1,1,0,0,0,1],
        [1,0,1,0,0,1],
        [1,1,0,1,0,1]
        ]
for poly in polies:
    print("Attempting to reduce polynomial "+format_polynomial(poly))
    s="Result: "
    res=factor_polynomial(poly,2,True)
    if res is None:
        s+="None"
    else:
        s+="("+format_polynomial(res[0])+")*("+format_polynomial(res[1])+")"
    print(s)
