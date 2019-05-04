def rabin_decrypt(y, p, q, verbose=False):
    if p % 4 != 3:
        return 'p must = 3 in mod 4'
    elif q % 4 != 3:
        return 'q must = 3 in mod 4'
    p_pos = pow(y,int((p+1)/4),p)
    q_pos = pow(y,int((q+1)/4),q)
    if verbose:
        print('√(' + str(y) + ') mod ' + str(p) + ' = ' +  str(y) + superscript(int((p+1)/4)) + ' mod ' + str(p))
        print('and √(' + str(y) + ') mod ' + str(q) + ' = ' +  str(y) + superscript(int((q+1)/4)) + ' mod ' + str(q))
        print('Set 1:')
        print('  x ≡ ' + str(p_pos) + ' mod ' + str(p))
        print('  x ≡ ' + str(q_pos) + ' mod ' + str(q))
        print('Set 2:')
        print('  x ≡ ' + str(-1*p_pos) + ' mod ' + str(p))
        print('  x ≡ ' + str(q_pos) + ' mod ' + str(q))
        print('Set 3:')
        print('  x ≡ ' + str(p_pos) + ' mod ' + str(p))
        print('  x ≡ ' + str(-1*q_pos) + ' mod ' + str(q))
        print('Set 4:')
        print('  x ≡ ' + str(-1*p_pos) + ' mod ' + str(p))
        print('  x ≡ ' + str(-1*q_pos) + ' mod ' + str(q))
    mod_values = [p,q]
    if verbose: print('\nSet 1 Solved:')
    set_1 = chinese_remainder([p_pos, q_pos], mod_values, verbose)
    if verbose: print('\nSet 2 Solved:')
    set_2 = chinese_remainder([-1*p_pos, q_pos], mod_values, verbose)
    if verbose: print('\nSet 3 Solved:')
    set_3 = chinese_remainder([p_pos, -1*q_pos], mod_values, verbose)
    if verbose: print('\nSet 4 Solved')
    set_4 = chinese_remainder([-1*p_pos, -1*q_pos], mod_values, verbose)
    return [set_1, set_2, set_3, set_4]

registerFunction("rabin_decrypt", {
"name" : "Decrypt Rabin Cryptosystem",
"arguments_short":["y","p", "q", "verbose=False"],
"arguments":["y=ciphertext=x^2 mod n", "p=prime s.t. p = 3 mod 4", "q=prime s.t. q = 3 mod 4", "give step-by-step instructions"],
"description":"Returns all decryptions of a given ciphertext"
})
