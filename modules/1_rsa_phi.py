def rsa_phi(p,q):
    return (p-1) * (q-1)

registerFunction("rsa_phi", {
    "name" : "Find PHI(n) for RSA",
    "arguments_short":["p","q"],
    "arguments":["p of rsa (rsa n = p*q)", "q of rsa (rsa n = p*q)"],
    "description":"Returns phi_n where phi_n = (p-1) * (q-1) for RSA"
})