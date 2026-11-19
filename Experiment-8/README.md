# Experiment: Secure Text Messages Using AES Encryption and SHA-256 Hashing

## 1. Aim

To develop a Python application that secures text messages using AES encryption and SHA-256 hashing to ensure message confidentiality and verify data integrity.

## 2. Introduction

Cryptography is used to protect sensitive information from unauthorized access. Encryption converts readable messages (plaintext) into an unreadable format (ciphertext), while hashing generates a fixed-length digest to verify data integrity.

In this experiment, Python is used to implement AES-based encryption and SHA-256 hashing. The application encrypts a user-provided message, decrypts it, and compares the original and decrypted message hashes.

## 3. Technologies Used

- Programming Language: Python
- IDE: Visual Studio Code
- Library: Cryptography
- Hashing Algorithm: SHA-256
- Encryption Algorithm: AES (Fernet)

## 4. Software Requirements

- Python 3.x
- Visual Studio Code
- Cryptography Python Library

## 5. Installation

Install the required Python library using:

```bash
pip install cryptography
```

## 6. Implementation

### Step 1: Import Libraries

```python
import hashlib
from cryptography.fernet import Fernet
```

### Step 2: Generate Encryption Key

```python
key = Fernet.generate_key()
cipher = Fernet(key)
```

### Step 3: Generate SHA-256 Hash

```python
hash_value = hashlib.sha256(message.encode()).hexdigest()
```

This generates a 256-bit hash value represented by 64 hexadecimal characters.

### Step 4: AES Encryption

```python
encrypted = cipher.encrypt(message.encode())
```

The original message is encrypted using the Fernet encryption mechanism, which internally uses AES-128-CBC with HMAC-SHA256 authentication.

### Step 5: AES Decryption

```python
decrypted = cipher.decrypt(encrypted).decode()
```

The encrypted message is converted back into its original readable form.

### Step 6: Hash Verification

```python
new_hash = hashlib.sha256(decrypted.encode()).hexdigest()

if hash_value == new_hash:
    print("Hash Verified Successfully!")
else:
    print("Hash Verification Failed!")
```

The original and decrypted message hashes are compared to verify message integrity.

## 7. Sample Output

```text
Enter your message: Hello Yogendra

Original Message: Hello Yogendra

SHA-256 Hash:
[64-character hexadecimal hash]

Encrypted Message:
[gAAAAAB... encrypted text]

Decrypted Message: Hello Yogendra

Hash Verified Successfully!
```

*Note: The actual hash and encrypted output are generated dynamically each time the program runs.*

## 8. Working Procedure

1. The user enters a text message.
2. The application generates a SHA-256 hash of the original message.
3. An encryption key is generated using Fernet.
4. The message is encrypted using AES.
5. The encrypted message is decrypted using the same key.
6. SHA-256 hashing is performed again on the decrypted message.
7. Both hash values are compared.
8. If both hashes match, message integrity is verified.

## 9. Algorithms Used

| Algorithm | Purpose |
|---|---|
| AES-128-CBC | Encrypts and decrypts messages |
| SHA-256 | Generates a 256-bit hash |
| HMAC-SHA256 | Authenticates encrypted data |
| Fernet | Provides authenticated symmetric encryption |

## 10. Results and Observations

- Successfully generated an encryption key.
- Successfully encrypted the input text message.
- Successfully generated a SHA-256 hash.
- Successfully decrypted the encrypted message.
- Successfully compared the original and decrypted message hashes.
- Message integrity was verified successfully.

## 11. Conclusion

In this experiment, a Python-based secure text messaging application was developed using AES encryption and SHA-256 hashing. The application successfully encrypted and decrypted text messages and verified their integrity by comparing SHA-256 hash values.

The experiment demonstrates how encryption and hashing techniques can be used together to improve the security of digital communication.

---

**Experiment:** Secure Text Message Encryption and Hashing  
**Subject:** Cryptography and Network Security  
**Language:** Python  
**IDE:** Visual Studio Code