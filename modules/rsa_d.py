def rsa_d(phi_n, e):
    return multiplicative_inverse(phi_n, e)

registerFunction("rsa_d", {
    "name" : "Find the decryption exponential for RSA",
    "arguments_short":["phi_n, e"],
    "arguments":["phi_n you can run rsa_phi for this", "the public RSA encryption exponential e"],
    "description":"Returns the decryption exponential for RSA"
})