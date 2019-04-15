def rsa_encrypt(plaintext_numbers, e, n, verbose=False):
    if type(plaintext_numbers) is int:
        plaintext_numbers = [plaintext_numbers]
    r=[pow(p, e, n) for p in plaintext_numbers]
    if verbose:
        for i in range(len(r)):
            p=plaintext_numbers[i]
            print("y=sam("+str(p)+","+str(e)+","+str(n)+")="+str(r))
    return r

def rsa_decrypt(ciphertext_numbers, d, n, verbose=False):
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
    "arguments_short":["data","e","n"],
    "arguments":["plaintext list in numbers", "encryption exponent e", "mod value"],
    "description":"Returns the ciphertext in numbers for a given plaintext"
})

registerFunction("rsa_decrypt", {
    "name" : "Decrypt RSA encrypted text",
    "arguments_short":["data","d","n"],
    "arguments":["ciphertext list in numbers", "decryption exponent d", "mod value"],
    "description":"Returns the plaintext in numbers of RSA encrypted text"
})
