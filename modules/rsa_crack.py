def rsa_crack(data, e, n):
    pqtup=rsa_pq(n)
    p=pqtup[0]
    q=pqtup[1]
    phi=rsa_phi(p,q)
    d=rsa_d(phi,e)
    return rsa_decrypt(data,d,n)

registerFunction("rsa_crack", {
    "name" : "Crack RSA",
    "arguments_short":["data","e","n"],
    "arguments":["ciphertext number list","encryption exponent","modulous"],
    "description":"Cracks ciphertext given e and n, returning number list"
})
