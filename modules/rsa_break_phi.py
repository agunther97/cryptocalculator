def rsa_break_phi(n, phi_n, verbose=False):
    A = 1
    B = phi_n - n - 1
    C = n
    plus_result = (-1*B + sqrt(pow(B,2) - (4*A*C)))/(2*A)
    minus_result = (-1*B - sqrt(pow(B,2) - (4*A*C)))/(2*A)
    if verbose:
        print(totient + '(n) = (p-1)(q-1) = pq-p-q+1')
        print('Since pq = n → n/p = q')
        print(totient + '(n) = n - p - n/p + 1')
        print('  → p' + totient + '(n) = pn - p' + superscript(2) + ' - n + 1')
        print('    → p' + superscript(2) + ' + p' + totient + '(n) - np - p + n = 0')
        print('      → p' + superscript(2) + ' + p(' + totient + '(n) - n - 1) + n')
        print('Let p = x, A = 1, B = (' + totient + '(n) - n - 1), C = n')
        print('Then x = (-B ± √(B' + superscript(2) + ' - 4AC))/2A = q (when using +) and p (when using -)')
        print('x = (-(' + str(B) + ') ± √(' + str(B) + superscript(2) + ' - ' + str(4*A*C) + ' = q (when using +) and p (when using -)')
    return [plus_result, minus_result]

registerFunction("rsa_break_phi", {
    "name" : "Break RSA using Quadratic Formula",
    "arguments_short":["n","phi_n","verbose=False"],
    "arguments":["n=p*q", "phi(n) or totient(n)","give step-by-step instructions"],
    "description":"Returns p and q for a given n"
})