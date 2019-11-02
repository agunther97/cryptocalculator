# Crypto Calculator

### Python terminal based calculator for Crypto cipher attacks and encryptions

## Usage

Navigate to the repository folder and run:

```bash
./cryptocalc
```

Your terminal should now be running the calculator. Use the `help` command to show a list of the supported functions, you can then use `help(functionName)` to show the details of a given command.

**Note:** Tab compleation is supported within the calculator for all function names, this will also work within the `help(functionName)` command

## Windows

Crypyto calc runs under bash, so currently we only support linux. If you want to try it on Windows be our guest but as of now you will definitily have to take on a pyreadline dependency with:

```python
pip install pyreadline
```

along with executing the cryptocalc script differently.

## Adding a method

```
TODO
```

## Currently Supported Functions

**Note:** For simplicity the optional verbose parameter has been left out of the following documentation. The verbose parameter will always default to false but calling a function with verbose = true will print out additional step information.

### Chinese Remainder
* chinese_remainder(number_values, mod_values)
    * Description:  Returns the solution to a set of congruences using chinease remainder theorem
    * Parameters:
        * number_values: The number values of the problem in a list (i.e. for x = 14 mod 29 you'd put 4), 
        * mod_values: The mod values of the problem in a list

### Clear
* clear()
    * Description: Clears the terminal

### Elgamal Generate Alpha
* elgamal_alpha(p)
    * Description: Computes first primitive root of a prime
    * Parameters:
        * p: The prime

### Elgamal Generate Beta
* elgamal_beta(p, alpha, a)
    * Description: Computes `beta` for Elgamal given `modulo`, `alpha`, and the elgamal secret `a`
    * Parameters:
        * p: Modulous 
        * Alpha
        * a: Secret

### Elgamal Crack A
* elgamal_crack_a(p, alpha, beta)
    * Description: Computes elgamal secret `a` using table crack method
    * Parameters:
        * p: Modulous
        * Alpha
        * Beta

###  Elgamal Decryption
* elgamal_decrypt(data, p, a)
    * Description: Computes plaintext using Elgamal decryption
    * Parameters:
        * data: Ciphertext as a number list
        * p: Modulous
        * a: Elgamal secret

### Elgamal Encrypt
* elgamal_encrypt(data, p, alpha, a, k=None)
    * Description: Computes ciphertext using Elgamal encryption
    * Parameters: 
        * data: Plaintext number list
        * p: Modulous
        * Alpha,
        * a: Secret 
        * k: Random value

### Elgamal Signature
* elgamal_sign(x, p, alpha, a, k=None)
    * Description: Returns signed tuple (gamma/delta) for given message
    * Parameters:
        * x: The message as a string or list of converted numbers
        * p: Modulous
        * Alpha
        * a: Secret
        * k: Random value

### Elgamal Verify Signature
* elgamal_verify(x, tuple, p, alpha, beta)
    * Description: Verifies signature for a given message + tuple
    * Parameters:
        * x: The message as a string or list of converted numbers
        * tuple: signature
        * p: modulous
        * Alpha
        * Beta

* elgamald(data,p,a),
* elgamale(data,p,alpha,a,k=None,verbose=False),
* euler_criterion(x,p,verbose=False), inv(x,y),
* irreducible_poly(deg,field,fast=True,verbose=False), lower(s),
* multiplicative_inverse(x,y),
* ntt_book(data,segLen=3,alpha=alphabet), phi(n,verbose=False),
* primitive_elements(mod,verbose=False),
* quadratic_residues(modulo,verbose=False),
* rabin_decrypt(y,p,q,verbose=False),
* rabin_encrypt(x,p,q,verbose=False),
* rsa_break_phi(n,phi_n,verbose=False),
* rsa_crack(data,n,e,verbose=False), rsa_d(phi_n,e,verbose=False),
* rsa_decrypt(data,n,d,verbose=False),
* rsa_encrypt(data,n,e,verbose=False), rsa_n(p,q,verbose=False),
* rsa_phi(p,q,verbose=False), rsa_pq(n,verbose=False),
* sam(x,c,n), ttn_book(data,segLen=3,alpha=alphabet),
* upper(s), vigenere_decrypt(s,k,alphabet,verbose=False),
* vigenere_encrypt(s,k,alphabet,verbose=False),
* vigenere_key(p,c,alphabet,verbose=False)