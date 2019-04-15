def rsa_crack(ciphertext_numbers, d, n):
    return [pow(c, d, n) for c in ciphertext_numbers]

registerFunction("rsa_crack", {
    "name" : "Crack RSA encrypted text",
    "arguments_short":["ciphertext_numbers","d","n"],
    "arguments":["cipher text list in numbers", "decryption exponent d", "mod value"],
    "description":"Returns the plain text in numbers of RSA encrypted text"
})
