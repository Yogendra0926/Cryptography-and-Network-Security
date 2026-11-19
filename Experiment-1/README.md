# EXP-1: Implementation of Classical Ciphers

## Aim
To implement Caesar Cipher, Vigenère Cipher, and Rail Fence Cipher for encryption and decryption, using the given plaintext **"HELLO WORLD"**, and compare their working and effectiveness.

## Plaintext
```text
HELLO WORLD
```

## 1. Caesar Cipher
Caesar Cipher is a substitution cipher that shifts each letter of the plaintext by a fixed number of positions in the alphabet.

- **Plaintext:** `HELLO WORLD`
- **Key:** 3
- **Encryption:** Each letter is shifted three positions forward.
- **Decryption:** Each letter is shifted three positions backward.

**Encrypted text:**
```text
KHOOR ZRUOG
```

### Screenshot
![Caesar Cipher Screenshot](screenshots/caesar.png)

## 2. Vigenère Cipher
Vigenère Cipher is a polyalphabetic substitution cipher that uses a keyword to determine the shift applied to each letter.

- **Plaintext:** `HELLO WORLD`
- **Key:** `KEY`
- **Encryption:** The keyword is repeated across the plaintext letters, ignoring spaces.
- **Decryption:** The same keyword is used to recover the original plaintext.

**Encrypted text:**
```text
RIJVS UYVJN
```

### Screenshot
![Vigenere Cipher Screenshot](screenshots/vigenere.png)

## 3. Rail Fence Cipher
Rail Fence Cipher is a transposition cipher that rearranges the positions of letters according to a zigzag pattern across multiple rails.

- **Plaintext:** `HELLO WORLD`
- **Key:** 2 rails
- **Encryption:** Letters are arranged in a zigzag pattern and then read row by row.
- **Decryption:** The zigzag arrangement is reconstructed to recover the original plaintext.

**Encrypted text (2 rails, spaces removed):**
```text
HLOWRD EL OL
```

### Screenshot
![Rail Fence Cipher Screenshot](screenshots/rail-fence.png)

## Comparison

| Feature | Caesar Cipher | Vigenère Cipher | Rail Fence Cipher |
|---|---|---|---|
| Cipher type | Substitution | Polyalphabetic substitution | Transposition |
| Key | Fixed shift | Keyword | Number of rails |
| Working | Shifts letters | Uses varying shifts based on a keyword | Rearranges letter positions |
| Security | Very weak | Stronger than Caesar, but weak with short/repeated keys | Very weak |
| Main limitation | Easily broken by brute force | Vulnerable to cryptanalysis with weak keys | Letter order can be reconstructed |

## Conclusion
Caesar, Vigenère, and Rail Fence are classical encryption techniques that demonstrate different approaches to protecting plaintext. Caesar and Vigenère change the letters through substitution, whereas Rail Fence changes their positions through transposition. These methods are useful for understanding cryptography fundamentals but are not secure enough for modern applications.
