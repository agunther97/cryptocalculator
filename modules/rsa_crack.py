def rsa_crack(cipher_text_numbers, d, n):
    return [sam(c, d, n) for c in cipher_text_numbers]

registerFunction("rsa_crack", {
    "name" : "Crack RSA encrypted text",
    "arguments_short":["cipher_text_numbers, d, n"],
    "arguments":["cipher text list in numbers", "decryption exponent d", "mod value"],
    "description":"Returns the plain text in numbers of RSA encrypted text"
})