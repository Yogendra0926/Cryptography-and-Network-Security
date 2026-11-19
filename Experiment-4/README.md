# Experiment 4: RSA File Encryption and Decryption Using OpenSSL

## Aim
To generate RSA public and private key pairs and perform file encryption and decryption using OpenSSL.

## Software Required
- OpenSSL
- Windows Command Prompt (CMD)
- Text editor (VS Code)

## Theory
RSA is an asymmetric cryptographic algorithm that uses two keys:
- **Public Key:** Used to encrypt data.
- **Private Key:** Used to decrypt data.

The public key can be shared, while the private key must be kept secret.

## Procedure

### Step 1: Generate the RSA Private Key

```cmd
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
```

This command generates a 2048-bit RSA private key and saves it as `private_key.pem`.

### Step 2: Generate the RSA Public Key

```cmd
openssl pkey -in private_key.pem -pubout -out public_key.pem
```

This command extracts the public key from the private key and saves it as `public_key.pem`.

### Step 3: Create the Input File

Create a text file named `message.txt` containing sample text, for example:

```text
This is a sample message for RSA encryption.
```

### Step 4: Encrypt the File

```cmd
openssl pkeyutl -encrypt -in message.txt -pubin -inkey public_key.pem -out encrypted.bin
```

This command encrypts the message using the RSA public key and stores the ciphertext in `encrypted.bin`.

**Note:** Direct RSA encryption only supports small inputs. With a 2048-bit RSA key and OAEP-SHA256 padding, the maximum plaintext size is 190 bytes. For larger files, use hybrid encryption with AES for the file and RSA for the AES key.

### Step 5: Decrypt the File

For an encrypted file created using the command above, decrypt it with:

```cmd
openssl pkeyutl -decrypt -in encrypted.bin -inkey private_key.pem -out decrypted.txt
```

This command uses the private key to recover the original message.

### Step 6: Verify the Result

Display the decrypted message:

```cmd
type decrypted.txt
```

Compare the original and decrypted files:

```cmd
fc /b message.txt decrypted.txt
```

If the files match, the original data has been recovered successfully.

## Files Created

- `private_key.pem` — RSA private key
- `public_key.pem` — RSA public key
- `message.txt` — Original plaintext
- `encrypted.bin` — Encrypted ciphertext
- `decrypted.txt` — Decrypted plaintext

## Result
RSA public and private key pairs were generated using OpenSSL. The sample message was encrypted with the public key and decrypted with the private key.

## Screenshots
Save screenshots of successful key generation, encryption, and decryption in the `screenshots/` folder.

## Security Note
Never share or upload your private key to a public repository. These commands demonstrate RSA with a small message; use hybrid encryption for larger files.