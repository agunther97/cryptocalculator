def rsa_crack(data, e, n):
    pqtup=rsa_pq(n)
    p=pqtup[0]
    q=pqtup[1]
    phi=rsa_phi(p,q)
    d=rsa_d(phi,e)
    return rsa_decrypt(data,d,n)