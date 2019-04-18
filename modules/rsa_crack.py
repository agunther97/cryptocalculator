def rsa_crack(data, e, n, verbose=False):
    pqtup=rsa_pq(n,verbose=verbose)
    p=pqtup[0]
    q=pqtup[1]
    phi=rsa_phi(p,q,verbose=verbose)
    d=rsa_d(phi,e,verbose=verbose)
    return rsa_decrypt(data,n,d,verbose=verbose)

registerFunction("rsa_crack", {
    "name" : "Crack RSA",
    "arguments_short":["data","e","n","verbose=False"],
    "arguments":["ciphertext number list","encryption exponent","modulous","print commands"],
    "description":"Cracks ciphertext given e and n, returning number list"
})
