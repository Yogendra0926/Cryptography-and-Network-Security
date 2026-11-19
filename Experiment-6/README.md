# Experiment 6: Self-Signed X.509 Digital Certificate Using OpenSSL

## Aim
To create a self-signed X.509 digital certificate and analyze its attributes, validity, and security features using OpenSSL.

## Software Required
- OpenSSL
- Windows Command Prompt (CMD)
- Visual Studio Code (optional)

## Theory
An X.509 digital certificate is an electronic document that associates an identity with a public key. It contains information such as the subject, issuer, validity period, public key, and digital signature.

A self-signed certificate is signed using its own corresponding private key rather than a certificate authority (CA). It can be useful for testing and learning, but it is not automatically trusted by browsers or operating systems.

## Procedure

### Step 1: Generate a Private Key

```cmd
openssl genrsa -out private.key 2048
```

This command generates a 2048-bit RSA private key and saves it in `private.key`.

### Step 2: Create a Self-Signed Certificate

```cmd
openssl req -new -x509 -key private.key -out certificate.crt -days 365
```

Enter the requested certificate details, such as:

- Country Name
- State or Province
- Organization
- Organizational Unit
- Common Name (CN)
- Email Address (if requested)

The command creates a self-signed certificate valid for 365 days.

### Step 3: Inspect the Certificate

```cmd
openssl x509 -in certificate.crt -text -noout
```

Observe the following certificate attributes:

- **Subject:** Identity described by the certificate.
- **Issuer:** Entity that issued and signed the certificate.
- **Serial Number:** Certificate identifier.
- **Validity Period:** Start and expiration dates.
- **Public Key:** Public key included in the certificate.
- **Signature Algorithm:** Algorithm used to sign the certificate.

### Step 4: Check the Subject and Issuer

```cmd
openssl x509 -in certificate.crt -noout -subject -issuer
```

For a self-signed certificate, the Subject and Issuer should identify the same entity.

## Expected Output

Two files are created:

| File | Description |
|---|---|
| `private.key` | Private RSA key used to sign the certificate |
| `certificate.crt` | Self-signed X.509 digital certificate |

The certificate inspection command displays its subject, issuer, serial number, validity period, public key information, and signature algorithm.

## Security Analysis

- The private key must remain confidential.
- The certificate's validity dates indicate when it is valid according to its time period.
- A self-signed certificate does not establish trust through a trusted certificate authority.
- A 2048-bit RSA key is commonly used for security, but overall security also depends on the signature algorithm, key protection, certificate configuration, and how the certificate is trusted.

## Result
A self-signed X.509 digital certificate was created successfully using OpenSSL, and its important attributes, validity period, and security features were inspected.

## Screenshots
Save screenshots of the following steps in the `screenshots/` folder:

1. Private key generation
2. Certificate creation
3. Certificate attribute inspection
4. Subject and Issuer verification

## Security Note
Do not upload `private.key` to a public GitHub repository. Keep the private key secure and exclude it from version control.