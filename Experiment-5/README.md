# Experiment–5: SHA-256 Hashing and Digital Signature Using OpenSSL

## 1. Aim

To generate SHA-256 hash values, create digital signatures, and verify their authenticity using OpenSSL.

## 2. Introduction

Cryptographic hashing and digital signatures are important techniques used in information security to maintain data integrity, authenticity, and non-repudiation.

In this experiment, OpenSSL is used to generate SHA-256 hash values and implement RSA-based digital signatures. A message is signed using a private key and its authenticity is verified using the corresponding public key.

## 3. Software Requirements

- Operating System: Windows
- Software: OpenSSL
- Interface: Command Prompt (CMD)
- Algorithm: SHA-256
- Digital Signature Algorithm: RSA
- RSA Key Size: 2048 bits

## 4. Concepts Used

### A. SHA-256 Hashing

SHA-256 (Secure Hash Algorithm 256-bit) is a cryptographic hash function that generates a fixed-length 256-bit (64 hexadecimal characters) digest from input data.

**Features:**
- Produces a 256-bit hash value.
- One-way cryptographic function.
- Small changes in input produce significantly different hash values.
- Used for data integrity verification.

### B. RSA Digital Signature

RSA is a public-key cryptographic algorithm used to create and verify digital signatures.

**Features:**
- Uses a pair of public and private keys.
- Private key is used for signing.
- Public key is used for verification.
- Helps verify message integrity and authenticity.

## 5. Implementation Steps

### Step 1: Check OpenSSL Installation

```cmd
openssl version
```

### Step 2: Create Experiment Directory

```cmd
mkdir Experiment-5
cd Experiment-5
```

### Step 3: Create Sample Message

```cmd
echo This is my secret message 123123 > message.txt
```

Display the message:

```cmd
type message.txt
```

### Step 4: Generate SHA-256 Hash

```cmd
openssl dgst -sha256 message.txt
```

Save the hash output:

```cmd
openssl dgst -sha256 message.txt > hash.txt
```

**Generated SHA-256 Hash:**

```text
02e57d8a03895879292d58e7c6d787df5a67de21563a717c019d66e734bb9f71
```

### Step 5: Generate RSA Private Key

Generate a 2048-bit RSA private key:

```cmd
openssl genrsa -out private_key.pem 2048
```

### Step 6: Generate RSA Public Key

Extract the public key from the private key:

```cmd
openssl rsa -in private_key.pem -pubout -out public_key.pem
```

### Step 7: Create Digital Signature

Sign the original message using the private key and SHA-256:

```cmd
openssl dgst -sha256 -sign private_key.pem -out signature.bin message.txt
```

The generated digital signature is stored in `signature.bin`.

### Step 8: Verify Digital Signature

Verify the signature using the public key:

```cmd
openssl dgst -sha256 -verify public_key.pem -signature signature.bin message.txt
```

**Expected Output:**

```text
Verified OK
```

This confirms that the signature is valid for the original message and corresponding public key.

### Step 9: Test Message Authenticity

Modify the original message:

```cmd
echo This message has been modified. > message.txt
```

Verify the signature again:

```cmd
openssl dgst -sha256 -verify public_key.pem -signature signature.bin message.txt
```

**Expected Output:**

```text
Verification failure
```

The verification fails because the message has been modified after the digital signature was created.

OpenSSL may also display additional diagnostic error messages depending on its version.

## 6. Results and Observations

| Operation | Result |
|---|---|
| SHA-256 Hash Generation | Successful |
| RSA Private Key Generation | Successful |
| RSA Public Key Generation | Successful |
| Digital Signature Creation | Successful |
| Original Message Verification | Verified OK |
| Modified Message Verification | Verification Failure |

### Important Observations

1. SHA-256 successfully generated a 256-bit hash value.
2. RSA successfully generated a 2048-bit private and public key pair.
3. The original message passed digital signature verification.
4. Modifying the message caused signature verification to fail.
5. Digital signatures help establish message integrity and verify that the signature was created using the corresponding private key.

## 7. Project Structure

```text
Experiment-5/
│
├── README.md
├── message.txt
├── hash.txt
├── public_key.pem
├── private_key.pem
└── signature.bin
```

**Security Note:** Never upload your private key (`private_key.pem`) to a public GitHub repository. Keep it confidential.

## 8. Conclusion

In this experiment, SHA-256 hashing and RSA-based digital signature operations were successfully implemented using OpenSSL. A SHA-256 hash was generated, an RSA key pair was created, and a digital signature was generated using the private key.

The signature was successfully verified using the corresponding public key. When the original message was modified, verification failed, demonstrating the importance of digital signatures in ensuring data integrity and authenticity.

---

**Subject:** Cryptography and Network Security  
**Experiment Number:** 05  
**Tools Used:** OpenSSL and Windows Command Prompt  
**Hashing Algorithm:** SHA-256  
**Digital Signature Algorithm:** RSA (2048-bit)