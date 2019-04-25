polies=[
        #the 4 below this come from the book, and check out with what the textbook informs.
        #[1,0,0,1],
        #[1,0,1,1],
        #[1,1,0,1],
        #[1,1,1,1]
        [1,1,0,0,0,1],
        [1,0,1,0,0,1],
        [1,1,0,1,0,1]
        ]
for poly in polies:
    print("Attempting to reduce polynomial "+format_polynomial(poly))
    s="Result: "
    res=factor_polynomial(poly,2,verbose=False)
    if res is None:
        s+="None. Thus, irreducible."
    else:
        s+="Reducible into ("+format_polynomial(res[0])+")*("+format_polynomial(res[1])+")"
    print(s)
