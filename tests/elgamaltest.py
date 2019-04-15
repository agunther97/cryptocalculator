txt=input("Enter a test string:\n")

p=55207
a=69
k=None
alpha=elgamal_alpha(p)

n=ttn(txt,3)
y=elgamale(n,p,alpha,elgamal_beta(p,alpha,a),verbose=True,k=k)
x=elgamald(y,p,a)
print(ntt(x))
