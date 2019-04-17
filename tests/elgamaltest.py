txt=input("Enter a test string:\n")
prime=input("Enter a prime:\n")
secret=input("Enter a number secret:\n")

try:
    p=int(prime)
except:
    p=55207
if p is None:
    p=55207

try:
    a=int(secret)
except:
    a=69
if p is None:
    a=69
k=elgamal_k(p,a)
alpha=elgamal_alpha(p,verbose=True)

n=ttn(txt,3)
y=elgamal_encrypt(n,p,alpha,a,verbose=True,k=k)
x=elgamald(y,p,a,verbose=True)
print(ntt(x))
