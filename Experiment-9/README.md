# Experiment–9: Password Hashing With and Without Salting Using Python

## 1. Aim

To implement password hashing with and without salting using Python and evaluate its resistance against common password attacks such as dictionary attacks, brute-force attacks, and rainbow table attacks.

## 2. Introduction

Password hashing is a security technique used to protect user passwords by converting them into fixed-length hash values.

Salting is an additional security technique in which a random value is added to a password before hashing. It ensures that identical passwords generate different hash values when different salts are used.

In this experiment, Python is used to implement both methods and compare their security features.

## 3. Technologies Used

- Programming Language: Python
- IDE: Visual Studio Code
- Hashing Algorithm: SHA-256
- Password Hashing Algorithm: PBKDF2-HMAC-SHA256
- Modules: hashlib, secrets, hmac

## 4. Software Requirements

- Python 3.x
- Visual Studio Code

## 5. Concepts Used

### A. Password Hashing Without Salt

In this method, the password is directly converted into a SHA-256 hash.

**Features:**
- Uses SHA-256 hashing.
- Same password always generates the same hash.
- Vulnerable to precomputed rainbow table attacks.
- Fast to calculate, making password guessing easier.

### B. Password Hashing With Salt

In this method, a randomly generated salt is combined with the password before applying PBKDF2-HMAC-SHA256.

**Features:**
- Uses a random 16-byte salt.
- Generates different hashes for identical passwords when salts differ.
- Makes precomputed rainbow table attacks ineffective.
- PBKDF2 increases the computational cost of password guessing.

## 6. Implementation

### Step 1: Import Required Libraries

```python
import hashlib
import secrets
import hmac
```

### Step 2: Hash Without Salt

```python
def hash_without_salt(password):
    return hashlib.sha256(password.encode()).hexdigest()
```

### Step 3: Hash With Salt

```python
def hash_with_salt(password):
    salt = secrets.token_bytes(16)

    hashed = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000
    )

    return salt, hashed
```

### Step 4: Verify Password

```python
def verify_password(password, salt, stored_hash):
    new_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000
    )

    return hmac.compare_digest(new_hash, stored_hash)
```

### Step 5: Dictionary Attack Demonstration

The program uses a predefined list of common passwords to demonstrate how an unsalted SHA-256 hash can be matched against common password guesses.

## 7. Sample Output

**Input:**

```text
Enter your password: 1020abc
```

### A. Without Salt

```text
--- WITHOUT SALT ---

Hash 1: d1420181360fd1a7e8a407c7bf47586ed99eba817bad573c39e94c26af2b785a

Hash 2: d1420181360fd1a7e8a407c7bf47586ed99eba817bad573c39e94c26af2b785a

Same Hash: True
```

### B. With Salt

```text
--- WITH SALT ---

Salt 1: 13f9c4df52129c9ac291a54fef3fd208

Hash 1: 1bd87225d9acc3f2995c81eb4ae51bc779b4e0517d90a4a00166470d3c8d389e

Salt 2: 1681dae98c9aa3b405d32080ab649193

Hash 2: be89e2c9dde256ea5b09a1ca66b4265fb43f154cd774c04903ee83be4f06d75f

Same Hash: False
```

### C. Password Verification

```text
--- PASSWORD VERIFICATION ---

Re-enter your password: 1020aaa

Incorrect Password!
```

The verification failed because the entered password did not match the original password.

### D. Dictionary Attack Demonstration

```text
--- DICTIONARY ATTACK DEMO ---

Password found: password
```

The predefined dictionary successfully matched the unsalted hash of the common password `password`.

## 8. Comparison Between Hashing Methods

| Feature | Without Salt | With Salt |
|---|---|---|
| Algorithm | SHA-256 | PBKDF2-SHA256 |
| Random Salt | No | Yes |
| Same Password | Same Hash | Different Hashes |
| Rainbow Table Resistance | Low | High |
| Dictionary Attack Resistance | Low | Improved |
| Brute-force Resistance | Low | Improved |

## 9. Evaluation Against Common Password Attacks

**1. Dictionary Attack:**  
Without salting, common passwords can be matched against precomputed hashes. Salting prevents direct reuse of precomputed hash tables, although weak passwords can still be guessed.

**2. Brute-force Attack:**  
An attacker tries multiple password combinations. PBKDF2 makes each password guess more computationally expensive.

**3. Rainbow Table Attack:**  
Rainbow tables contain precomputed password-hash combinations. Random salts make these precomputed tables impractical to reuse.

## 10. Results and Observations

1. SHA-256 generated identical hashes for identical passwords without salting.
2. Random salts generated different hash values for the same password.
3. Password verification successfully detected an incorrect password.
4. The dictionary attack demonstration identified the common password `password`.
5. Salted PBKDF2 hashing provided better resistance against common password attacks.

## 11. Conclusion

In this experiment, password hashing was successfully implemented using Python with and without salting. The results demonstrated that unsalted hashing generates identical hashes for identical passwords, whereas salted hashing produces different hash values using random salts.

The experiment also demonstrated the advantages of PBKDF2 in increasing the computational cost of password guessing and protecting against precomputed rainbow table attacks.

---

**Experiment Number:** 09  
**Subject:** Cryptography and Network Security  
**Programming Language:** Python  
**IDE:** Visual Studio Code  
**Hashing:** SHA-256 and PBKDF2-HMAC-SHA256