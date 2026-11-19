# Experiment: Password Auditing Using John the Ripper in Kali Linux

## 1. Aim

To perform password auditing using John the Ripper and evaluate password strength against dictionary and brute-force attacks in Kali Linux.

## 2. Introduction

Password auditing is the process of checking passwords to determine whether they are weak, predictable, or vulnerable to attacks.

John the Ripper is a password auditing tool that can test password hashes against different password-guessing techniques, including dictionary attacks and brute-force attacks.

In this experiment, a password is converted into a salted SHA-512 crypt hash using OpenSSL. John the Ripper is then used with a dictionary file to attempt to recover the original password.

## 3. Requirements

- Kali Linux
- John the Ripper
- OpenSSL
- RockYou password wordlist
- Terminal

## 4. Theory

### Password Hashing

Password hashing converts a password into a fixed-length hash value. Hashes are designed to be one-way, meaning the original password should not be directly recoverable from the hash.

### Salt

A salt is a random value added during password hashing. It helps prevent attackers from using precomputed hash tables to attack multiple passwords efficiently.

### Dictionary Attack

A dictionary attack attempts passwords from a predefined list of commonly used passwords. If the actual password is present in the wordlist, it may be successfully recovered.

### Brute-Force Attack

A brute-force attack systematically tries different possible password combinations until a match is found. The time required depends on password length, complexity, and the hashing algorithm's computational cost.

## 5. Procedure

### Step 1: Create a working directory

Create a directory for the password auditing experiment.

```bash
mkdir password_audit
cd ~/password_audit
```

### Step 2: Generate a salted password hash

Generate a SHA-512 crypt password hash using OpenSSL.

```bash
openssl passwd -6 -salt s1bqi password
```

The generated hash contains the salt and the hashed password.

### Step 3: Save the hash into a file

Save the generated hash in `hashes.txt`.

```bash
echo '$6$s1bqi$GENERATED_HASH_HERE' > hashes.txt
```

Replace `GENERATED_HASH_HERE` with the complete hash generated in Step 2.

### Step 4: Perform a dictionary attack

Use John the Ripper with the RockYou wordlist to test common passwords against the hash.

```bash
john --format=sha512crypt --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```

John reads the hashes and compares them with password candidates generated from the wordlist.

### Step 5: Display the cracked password

Display any recovered password using:

```bash
john --show --format=sha512crypt hashes.txt
```

If the password is successfully recovered, John displays the cracked password and the number of hashes recovered.

## 6. Attack Types

| Attack | Description |
|---|---|
| Dictionary Attack | Tests passwords from a predefined wordlist such as RockYou. |
| Brute-Force Attack | Systematically tries possible password combinations. |
| Hybrid Attack | Combines dictionary words with additional characters, numbers, or symbols. |

## 7. Observation

During the experiment, one password hash was loaded by John the Ripper. The dictionary attack was performed using the RockYou wordlist.

The tool successfully recovered the weak password, and the result was verified using the `--show` option.

**Observed output:**

```text
1 password hash cracked, 0 left
```

## 8. Result Analysis

The experiment demonstrated that a weak password can be recovered even when it is stored as a hash.

- Dictionary attacks are effective against common and predictable passwords.
- Brute-force attacks can eventually recover passwords with sufficiently small search spaces.
- Longer passwords with unpredictable combinations are harder to crack.
- Salting helps protect against precomputed attacks, but it does not make weak passwords impossible to crack.
- Password hashing algorithms with high computational cost improve resistance to password guessing.

## 9. Security Recommendations

- Use long passwords with at least 12–16 characters where possible.
- Avoid dictionary words, common passwords, names, and predictable patterns.
- Use a unique password for every account.
- Use a password manager to generate and store strong passwords.
- Store passwords using secure password hashing algorithms such as Argon2id, bcrypt, or scrypt.
- Use multi-factor authentication (MFA) wherever available.

## 10. Conclusion

Password auditing was successfully performed using John the Ripper in Kali Linux. A salted SHA-512 crypt password hash was generated and tested using a dictionary attack with the RockYou wordlist.

The password was successfully cracked, demonstrating that weak and commonly used passwords are vulnerable to dictionary attacks. The experiment also highlighted the importance of password length, complexity, salting, and secure password storage in protecting user credentials.
