def rsa_n(p,q,verbose=False):
    if verbose:
        print("n=("+str(p)+")("+str(q)+")="+str((p) * (q)))
    return (p)*(q)

registerFunction("rsa_n", {
    "name" : "Find n for RSA",
    "arguments_short":["p","q","verbose=False"],
    "arguments":["p of rsa (rsa n = p*q)", "q of rsa (rsa n = p*q)","print command"],
    "description":"Returns n where n = (p) * (q) for RSA"
})