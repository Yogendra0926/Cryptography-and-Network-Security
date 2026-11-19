# Experiment: DES and AES Encryption Algorithms

## 1. Aim

To encrypt sample data using **Data Encryption Standard (DES)** and **Advanced Encryption Standard (AES)** algorithms and compare their security features, encryption mechanisms, and performance.

## 2. Introduction

Encryption is a fundamental technique in cryptography used to protect sensitive information from unauthorized access. It converts readable data (plaintext) into an unreadable format (ciphertext) using an encryption algorithm and a secret key.

In this experiment, two symmetric-key encryption algorithms are implemented:

- **DES (Data Encryption Standard):** An older symmetric block cipher that uses a 64-bit key, with 56 effective key bits.
- **AES (Advanced Encryption Standard):** A modern symmetric block cipher supporting 128-bit, 192-bit, and 256-bit key sizes.

Both algorithms are used to encrypt the same sample plaintext, and their security characteristics are compared.

## 3. Software Requirements

- CrypTool 2
- Windows Operating System
- Basic knowledge of Cryptography and Network Security

## 4. Algorithms Used

### A. Data Encryption Standard (DES)

DES is a symmetric-key block cipher that operates on 64-bit data blocks.

**Features:**
- Block Size: 64 bits
- Effective Key Size: 56 bits
- Structure: Feistel Network
- Number of Rounds: 16
- Encryption and decryption use the same secret key.

**Sample Configuration:**

| Parameter | Value |
|---|---|
| Plaintext | Yogendra |
| Secret Key | 12345678 |
| Algorithm | DES |
| Action | Encrypt |
| Chaining Mode | ECB |
| Padding | Zeros |
| Output Format | Hexadecimal |

**Encryption Output:**
```text
87 B8 F1 3E 0A A3 26 4E
```

### B. Advanced Encryption Standard (AES)

AES is a widely used symmetric-key block cipher designed to provide strong data security.

**Features:**
- Block Size: 128 bits
- Key Sizes: 128, 192, and 256 bits
- Structure: Substitution-Permutation Network
- Number of Rounds:
  - AES-128: 10 rounds
  - AES-192: 12 rounds
  - AES-256: 14 rounds

**Sample Configuration:**

| Parameter | Value |
|---|---|
| Plaintext | Yogendra |
| Algorithm | AES |
| Action | Encrypt |
| Key Size | 256 bits |
| Chaining Mode | ECB |
| Padding | Zeros |
| Output Format | Hexadecimal |

**Important:** AES-256 requires a 32-byte key. Use a valid 32-byte key for this configuration.

## 5. Implementation Procedure

### DES Encryption

1. Open CrypTool 2.
2. Add a Text Input component and enter `Yogendra`.
3. Connect it to a String Decoder.
4. Add another Text Input component for the secret key.
5. Enter `12345678` as the key.
6. Connect the key input to another String Decoder.
7. Add the DES encryption component.
8. Select the Encrypt action.
9. Configure ECB chaining mode and Zero padding.
10. Connect both plaintext and key inputs to the DES component.
11. Connect the output to a String Encoder.
12. Select Hexadecimal as the presentation format.
13. Connect it to Text Output to view the ciphertext.

### AES Encryption

1. Open CrypTool 2.
2. Add a Text Input component and enter `Yogendra`.
3. Connect it to a String Decoder.
4. Add another Text Input component for the AES secret key.
5. Provide a valid 32-byte key for AES-256.
6. Connect the key input to a String Decoder.
7. Add the AES encryption component.
8. Select the AES algorithm and Encrypt action.
9. Configure the key size to 256 bits.
10. Select ECB chaining mode and Zero padding.
11. Connect the plaintext and key inputs to the AES component.
12. Connect the output to a String Encoder.
13. Select Hexadecimal as the output format.
14. Connect it to Text Output to display the ciphertext.

## 6. Comparison Between DES and AES

| Feature | DES | AES |
|---|---|---|
| Full Form | Data Encryption Standard | Advanced Encryption Standard |
| Block Size | 64 bits | 128 bits |
| Key Size | 56 effective bits | 128/192/256 bits |
| Structure | Feistel Network | Substitution-Permutation Network |
| Rounds | 16 | 10/12/14 |
| Security | Weak / Obsolete | Strong |
| Performance | Depends on implementation | Generally efficient on modern hardware |
| Current Usage | Legacy systems | Modern encryption systems |

## 7. Security Analysis

**DES:**
- Has a relatively small effective key size.
- Vulnerable to brute-force attacks.
- No longer recommended for modern security applications.
- Mainly useful for understanding traditional encryption mechanisms.

**AES:**
- Supports significantly larger key sizes.
- Provides strong protection against practical brute-force attacks.
- Widely adopted in modern security applications.
- Suitable for protecting sensitive information when configured correctly.

## 8. Performance Analysis

Both algorithms perform symmetric-key encryption, but their performance depends on several factors:

- Input data size.
- Key size.
- Hardware configuration.
- Software implementation.
- Encryption mode.

AES generally provides better security and excellent performance on modern processors, particularly those with hardware AES acceleration.

**Note:** Actual execution time should be measured experimentally. No specific performance benchmark is claimed in this experiment.

## 9. Observations

1. DES successfully encrypts the sample plaintext using an 8-byte key.
2. AES successfully encrypts the sample plaintext using a valid AES key.
3. Both algorithms generate ciphertext that is different from the original plaintext.
4. DES uses a 64-bit block size, whereas AES uses a 128-bit block size.
5. AES provides significantly stronger security than DES.

## 10. Result

The sample plaintext was successfully encrypted using both DES and AES algorithms in CrypTool 2. Their encryption mechanisms, key sizes, security characteristics, and performance considerations were studied and compared.

It was concluded that AES is more secure and suitable for modern cryptographic applications, whereas DES is considered obsolete due to its limited key size.

## 11. Conclusion

This experiment demonstrates the implementation and comparison of two important symmetric-key encryption algorithms: DES and AES. Although both algorithms perform data encryption using secret keys, AES offers substantially stronger security and is the preferred choice for modern cryptographic applications.

---

**Tool Used:** CrypTool 2  
**Subject:** Cryptography and Network Security  
**Experiment:** DES and AES Encryption and Comparison