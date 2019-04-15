def rsa_d(phi_n, e):
    return inv(e,phi_n)

registerFunction("rsa_d", {
    "name" : "Find the decryption exponential for RSA",
    "arguments_short":["phi_n","e"],
    "arguments":["phi_n you can run rsa_phi for this", "the public RSA encryption exponential e"],
    "description":"Returns the decryption exponential for RSA"
})
