def rsa_encrypt(plaintext_numbers, n, e, verbose=False):
    if type(plaintext_numbers) is int:
        plaintext_numbers = [plaintext_numbers]
    r=[pow(p, e, n) for p in plaintext_numbers]
    if verbose:
        for i in range(len(r)):
            p=plaintext_numbers[i]
            print("y=sam("+str(p)+","+str(e)+","+str(n)+")="+str(r))
    return r

def rsa_decrypt(ciphertext_numbers, n, d, verbose=False):
    if type(ciphertext_numbers) is int:
        ciphertext_numbers = [ciphertext_numbers]
    r=[pow(p, d, n) for p in ciphertext_numbers]
    if verbose:
        for i in range(len(r)):
            p=ciphertext_numbers[i]
            print("x=sam("+str(p)+","+str(d)+","+str(n)+")="+str(r))
    return r

registerFunction("rsa_encrypt", {
    "name" : "Encrypt data with RSA",
    "arguments_short":["data","n","e","verbose=False"],
    "arguments":["plaintext list in numbers", "mod value", "encryption exponent e", "print commands"],
    "description":"Returns the ciphertext in numbers for a given plaintext"
})

registerFunction("rsa_decrypt", {
    "name" : "Decrypt RSA encrypted text",
    "arguments_short":["data","n","d","verbose=False"],
    "arguments":["ciphertext list in numbers", "mod value", "decryption exponent d", "print commands"],
    "description":"Returns the plaintext in numbers of RSA encrypted text"
})
