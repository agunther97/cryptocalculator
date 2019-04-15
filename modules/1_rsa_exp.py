def rsa_encrypt(plaintext_numbers, e, n):
    if type(plaintext_numbers) is int:
        plaintext_numbers = [plaintext_numbers]
    return [pow(p, e, n) for p in plaintext_numbers]
def rsa_decrypt(ciphertext_numbers, d, n):
    return rsa_encrypt(ciphertext_numbers, d, n)

registerFunction("rsa_encrypt", {
    "name" : "Encrypt data with RSA",
    "arguments_short":["data","d","n"],
    "arguments":["plaintext list in numbers", "encryption exponent e", "mod value"],
    "description":"Returns the ciphertext in numbers for a given plaintext"
})

registerFunction("rsa_decrypt", {
    "name" : "Decrypt RSA encrypted text",
    "arguments_short":["data","d","n"],
    "arguments":["ciphertext list in numbers", "decryption exponent d", "mod value"],
    "description":"Returns the plaintext in numbers of RSA encrypted text"
})
