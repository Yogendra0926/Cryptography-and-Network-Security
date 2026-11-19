# EXP-7: RSA and Diffie–Hellman Algorithms

## Aim
To implement RSA and Diffie–Hellman algorithms using Python in Visual Studio Code to demonstrate public-key cryptography and secure key exchange.

## Software Required
- Python 3
- Visual Studio Code

## Theory

**RSA Algorithm:** RSA is an asymmetric cryptographic algorithm that uses a public key for encryption and a private key for decryption. It is based on mathematical operations involving prime numbers.

**Diffie–Hellman Algorithm:** Diffie–Hellman is a key exchange algorithm that allows two parties, Alice and Bob, to calculate the same shared secret without directly transmitting it.

## Files
- `RSA.py` – Calculates RSA public and private keys, encrypts a numerical message, and decrypts the ciphertext.
- `DiffieHellman.py` – Calculates Alice's and Bob's public keys and verifies whether both parties obtain the same shared secret.

## Procedure

### Part A: RSA Algorithm
1. Open `RSA.py` in Visual Studio Code.
2. Set the prime numbers \(p=61\) and \(q=53\).
3. Calculate \(n=p\times q\) and Euler's totient \(\phi(n)\).
4. Calculate the private exponent using the modular inverse of the public exponent.
5. Enter a numerical plaintext smaller than \(n\).
6. Encrypt the message using the public key.
7. Decrypt the ciphertext using the private key and compare it with the original message.

### Part B: Diffie–Hellman Algorithm
1. Open `DiffieHellman.py` in Visual Studio Code.
2. Set the public prime \(p=23\) and generator \(g=5\).
3. Enter private keys for Alice and Bob.
4. Calculate their public keys using modular exponentiation.
5. Calculate the shared secret independently on both sides.
6. Compare both shared secrets to verify successful key exchange.

## Execution

Open the terminal in Visual Studio Code and run:

**RSA:**
```bash
python RSA.py
```

**Diffie–Hellman:**
```bash
python DiffieHellman.py
```

## Output and Observation

**RSA:** The program displays the prime numbers, modulus, totient, public key, private key, ciphertext, and decrypted numerical message. The decrypted message should match the original input.

**Diffie–Hellman:** The program displays Alice's and Bob's public keys and their calculated shared secrets. If both secrets match, the program displays `Key Exchange Successful!`.

## Result
RSA encryption and decryption were demonstrated using numerical plaintext. The Diffie–Hellman implementation successfully demonstrated shared-secret agreement between Alice and Bob.

## Conclusion
This experiment helped me understand RSA public-key cryptography, modular arithmetic, and the Diffie–Hellman key exchange process using Python.

## Screenshots
- `Screenshots/rsa-output.png`
- `Screenshots/diffie-hellman-output.png`
