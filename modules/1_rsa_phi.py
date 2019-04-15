def rsa_phi(p,q,verbose=False):
    if verbose:
        print("phi_n=("+str(p)+"-1)("+str(q)+"-1)="+str((p-1) * (q-1)))
    return (p-1) * (q-1)

registerFunction("rsa_phi", {
    "name" : "Find PHI(n) for RSA",
    "arguments_short":["p","q","verbose=False"],
    "arguments":["p of rsa (rsa n = p*q)", "q of rsa (rsa n = p*q)","print command"],
    "description":"Returns phi_n where phi_n = (p-1) * (q-1) for RSA"
})