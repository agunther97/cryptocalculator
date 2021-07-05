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

Crypytocalc was developed and tested primarily under Linux, split between Ubuntu and Arch. Though it will work under any platform which supports Python 3 or higher, this comes with a caveat: Windows lacks the readline libray by default, as well as support for the ANSI codes used for terminal colors.

The former issue results in a lack of tab completion, but may be fixed by the following command:

```python
pip install pyreadline
```

## Currently Supported Functions

**Note:** For simplicity the optional verbose parameter has been left out of the following documentation. The verbose parameter will always default to false but calling a function with verbose = true will print out additional step information.

### Chinese Remainder
* chinese_remainder(number_values, mod_values)
    * Description: Returns the solution to a set of congruences using chinease remainder theorem
    * Parameters:
        * number_values: The number values of the problem in a list (i.e. for x = 14 mod 29 you'd put 4)
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
        * Alpha
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
    * Description: Verifies signature for a given message and tuple
    * Parameters:
        * x: The message as a string or list of converted numbers
        * tuple: signature
        * p: modulous
        * Alpha
        * Beta

### Elgamal Decryption
* elgamald(data, p, a)
    * Description: Computes plaintext using Elgamal decryption
    * Parameters:
        * data: ciphertext number list
        * p: modulous
        * a: Secret

### Elgamal Encryption
* elgamale(data, p, alpha, a, k=None)
    * Description: Computes ciphertext using Elgamal encryption
    * Parameters: 
        * data: plaintext number list
        * Modulous
        * Alpha
        * Beta
        * k: Random value

### Euler's Criterion
* euler_criterion(x, p)
    * Description: Returns if number is a quadratic residue of a prime
    * Parameters:
        * x: number
        * p: modulo


### Find multiplicative Inverse
* inv(x, y) or multiplicative_inverse(x, y)
    * Description: Find multiplicative inverse
    * Parameters: 
        * x: value
        * y: mod
  
### Irreducible Polynomials over Field
* irreducible_poly(deg, field, fast=True)
    * Description: Returns the number of irreducible polynomials for a given field size
    * Parameters: 
        * deg: the degree of the polynominal
        * field: the field size (i.e. Z mod #)
        * fast: use fast algorithm default on, only calculates leading coeff. 1 and extrapolates

### Irreducible Polynomials over Field
* ntt_book(data, segLen=3, alpha=alphabet)
    * Description: Converts numbers to text using the book algorithm
    * Parameters: 
        * data: data to convert
        * segLen: letters per number
        * alpha: alphabet=list like [\"a\",\"b\",...]

### Phi
* phi(n)
    * Description: Computes Euler's totient of a number
    * Parameters:
        * n: number

### Find Primitive Elements
* primitive_elements(mod,verbose=False)
    * Description: Returns all primitive elements under a mod
    * Parameters
        * mod: modulous value
        * verbose: give step-by-step instructions

### Quadratic Residues
* quadratic_residues(modulo,verbose=False)
    * Description: Returns quadratic residues of a modulo
    * Parameters
        * modulo: modulous value
        * verbose: print commands

### Decrypt Rabin Cryptosystem
* rabin_decrypt("y","p", "q", "verbose=False")
	* Description: Returns all decryptions of a given ciphertext
	* Parameters
        * y: ciphertext=x^2 mod n
		* p: prime s.t. p = 3 mod 4
		* q: prime s.t. q = 3 mod 4
		* verbose: give step-by-step instructions

### Encrypt Rabin Cryptosystem
* rabin_encrypt("x","p", "q", "verbose=False")
	* Description: Returns encrypted ciphertext
	* Parameters
        * x: plaintext as numbers
		* p: prime s.t. p = 3 mod 4
		* q: prime s.t. q = 3 mod 4
		* verbose: give step-by-step instructions

### Convert number into RSA-Parsable blocks
* rsa_block(n,data,verbose=False)
    * Description: Returns array of numbers below n given large data value
    * Parameters
        * n: n=p*q
        * data: large number in int format
        * verbose: give step-by-step instructions

### Break RSA using Quadratic Formula
* rsa_break_phi(n,phi_n,verbose=False)
    * Description: Returns p and q for a given n
    * Parameters
        * n: n=p*q
        * phi_n: totient, calculated with phi(n) or totient(n)
        * verbose: give step-by-step instructions

### Crack RSA
* rsa_crack(data,n,e,verbose=False)
    * Description: Cracks ciphertext given e and n, returning number list
    * Parameters
        * data: ciphertext number list
        * n: modulous
        * e: encryption exponent
        * verbose: print commands

### Find Decryption Exponential for RSA
* rsa_d(phi_n,e,verbose=False)
    * Description: Returns the decryption exponential for RSA
    * Parameters
        * phi_n: totient, calculated with phi(n) or totient(n)
        * e: the public RSA encryption exponential e
        * verbose: print commands

### Decrypt RSA encrypted text
* rsa_decrypt(data,n,d,verbose=False)
    * Description: Decrypt RSA encrypted text
    * Parameters
        * data: ciphertext list in numbers
        * n: modulous value
        * d: decryption exponent d
        * verbose: print commands
        
### Encrypt data with RSA
* rsa_encrypt(data,n,e,verbose=False)
    * Description: Returns the ciphertext in numbers for a given plaintext
    * Parameters
        * data: plaintext list in numbers
        * n: modulous value
        * e: encryption exponent e
        * verbose: print commands

### Find N for RSA
* rsa_n(p,q,verbose=False)
    * Description: Returns n where n = (p) * (q) for RSA
    * Parameters
        * p: p of rsa (rsa n = p*q)
        * q: q of rsa (rsa n = p*q)
        * verbose: print commands

### Find PHI(n) for RSA
* rsa_phi(p,q,verbose=False)
    * Description: Returns the totient where the totient = (p-1) * (q-1) for RSA
    * Parameters
        * p: p of rsa (rsa n = p*q)
        * q: q of rsa (rsa n = p*q)
        * verbose: print commands

### Find P and Q for RSA
* rsa_pq(n,verbose=False)
    * Description: Returns (p,q) where n = pq for RSA
    * Parameters
        * n: product n=pq of RSA
        * verbose: print commands

### Convert number back from RSA blocks
* rsa_unblock(n,data,verbose=False)
    * Description: Returns large int value from array of rsa blocks. Pair with hex(n) for nice formatting.
    * Parameters
        * n: n=p*q
        * data: array of blocks
        * verbose: give step-by-step instructions

### Square and Multiply
* sam(x,c,n)
    * Description: Returns a float z s.t. x^c mod n = z
    * Parameters
        * x: base
        * e: exponent
        * m: mod

### Text to Numbers (Book)
* ttn_book( data,segLen=3, alpha=alphabet)
    * Description: Converts text to numbers using the book algorithm
    * Parameters
        * data: datato convert
        * segLen: letters per number
        * alphabet: alphabet, list like ["a","b","c"]

### Uppercase
* upper(s)
    * Description: Converts text to uppercase
    * Parameters
        * s: input string

### Encrypt Vigenere Cryptosystem
* vigenere_encrypt(s, k, alphabet, verbose=False)
	* Description: Returns encrypted ciphertext
	* Parameters
        * s: plaintext as text
		* k: key as text
		* alphabet: alphabet the system was encrypted with (default is mod 26)
        * verbose: give step-by-step instructions

### Decrypt Vigenere Cryptosystem
* vigenere_decrypt(s, k, alphabet, verbose=False)
	* Description: Returns decrypted plaintext
	* Parameters
        * s: ciphertext as text
		* k: key as text
		* alphabet: alphabet the system was encrypted with (default is mod 26)
        * verbose: give step-by-step instructions

### Find Vigenere Key with Plaintext and Ciphertext
* vigenere_key(p, c, alphabet, verbose=False)
	* Description: Returns key to Vigenere system
	* Parameters
        * p: plaintext as text
        * c: ciphertext as text
        * alphabet: alphabet the system was encrypted with (default is mod 26)
        * verbose: give step-by-step instructions
