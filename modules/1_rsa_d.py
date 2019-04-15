def rsa_d(phi_n, e, verbose=False):
    if verbose:
        print("d=inv("+str(e)+","+str(phi_n)+")="+str(inv(e,phi_n)))
    return inv(e,phi_n)

registerFunction("rsa_d", {
    "name" : "Find the decryption exponential for RSA",
    "arguments_short":["phi_n","e","verbose=False"],
    "arguments":["phi_n you can run rsa_phi for this", "the public RSA encryption exponential e","print commands"],
    "description":"Returns the decryption exponential for RSA"
})
