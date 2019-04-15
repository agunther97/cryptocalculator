p=5813
q=10133
strv="abc"

print("p="+str(p))
print("q="+str(q))
n=rsa_n(p,q,verbose=True)
phi=rsa_phi(p,q,verbose=True)
e=2
while gcd(e,phi)!=1:
    e=rand(p)
print("e="+str(e))
d=rsa_d(phi,e,verbose=True)
print("Plaintext string: " + strv)
out=rsa_encrypt(ttn(strv,3),e,n,verbose=True)
bak=ntt(rsa_decrypt(out,d,n,verbose=True))
print("Decrypted string: " + bak)