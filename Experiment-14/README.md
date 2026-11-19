# Experiment: Generate SSH/RSA Key Pairs and Configure Passwordless Authentication Between Linux Systems

## 1. Aim

To generate SSH/RSA key pairs and configure passwordless authentication between two Linux systems using SSH.

## 2. Introduction

SSH (Secure Shell) is a network protocol used to securely connect to and manage remote systems. It provides encrypted communication between a client and a server.

SSH supports key-based authentication, which allows users to log in to a remote Linux system without entering their account password every time.

In this experiment, an RSA key pair is generated on the client system. The public key is transferred to the remote Linux system and added to its authorized keys file. After configuration, the client can connect to the remote system using SSH key authentication.

## 3. Requirements

- Two Linux systems (Kali Linux or Ubuntu)
- SSH client
- OpenSSH server
- Network connectivity between both systems
- Terminal access

## 4. Theory

### SSH

SSH provides a secure, encrypted connection between two systems over a network. It is commonly used for remote login, command execution, and file transfer.

### RSA Key Pair

RSA is a public-key cryptographic algorithm that uses two mathematically related keys:

- **Public Key:** Shared with the remote system.
- **Private Key:** Kept secret on the local system.

The public key is placed on the remote system, while the private key remains on the client. During authentication, SSH verifies that the client possesses the corresponding private key.

### Passwordless Authentication

Passwordless SSH authentication uses public-key cryptography instead of repeatedly asking for the remote account password. The remote system checks the client's public key to authenticate the connection.

## 5. Procedure

### Step 1: Check SSH installation

Check whether SSH is installed on the Linux system.

```bash
ssh -V
```

### Step 2: Install OpenSSH

If SSH is not installed, install the required packages.

```bash
sudo apt update
sudo apt install openssh-client openssh-server -y
```

### Step 3: Start the SSH service

Start the SSH service on the remote Linux system.

```bash
sudo systemctl start ssh
```

Enable the SSH service at boot:

```bash
sudo systemctl enable ssh
```

Check its status:

```bash
sudo systemctl status ssh
```

### Step 4: Generate an RSA key pair

On the client Linux system, generate the RSA key pair.

```bash
ssh-keygen -t rsa -b 4096
```

Press Enter to accept the default key file location. You may set a passphrase or leave it empty for the lab demonstration.

The generated files are:

- `~/.ssh/id_rsa` – Private key
- `~/.ssh/id_rsa.pub` – Public key

### Step 5: Copy the public key to the remote system

Transfer the public key to the remote Linux system.

```bash
ssh-copy-id username@remote_ip
```

Replace `username` with the remote Linux username and `remote_ip` with the IP address of the remote machine.

Enter the remote account password when prompted for the initial setup.

### Step 6: Verify key files

Check the generated keys on the client system.

```bash
ls -l ~/.ssh/
```

Display the public key:

```bash
cat ~/.ssh/id_rsa.pub
```

The private key must not be shared.

### Step 7: Test passwordless SSH authentication

Connect to the remote Linux system:

```bash
ssh username@remote_ip
```

If the configuration is successful, the connection will authenticate using the SSH key without asking for the remote account password.

### Step 8: Verify remote connection

After connecting, execute the following command:

```bash
hostname
```

This displays the hostname of the remote system, confirming that the SSH connection is established.

Exit the remote system:

```bash
exit
```

## 6. Observation

During the experiment, an RSA key pair was successfully generated on the client Linux system. The public key was copied to the remote system and configured for SSH authentication.

The client was able to establish a remote connection without entering the remote account password, demonstrating successful key-based authentication.

## 7. Advantages of SSH Key-Based Authentication

- Provides secure authentication using cryptographic keys.
- Reduces the need to enter account passwords repeatedly.
- Helps prevent password-guessing attacks against SSH logins.
- Supports secure remote administration.
- Useful for automation, scripts, and server management.

## 8. Security Precautions

- Never share your private key.
- Use a passphrase to protect private keys whenever possible.
- Set appropriate permissions on SSH files.
- Use strong cryptographic keys.
- Disable password-based SSH login only after confirming key-based access works and ensuring you have an alternate recovery method.

## 9. Result

RSA key pairs were successfully generated, and SSH key-based authentication was configured between Linux systems. Passwordless authentication was tested, and a secure remote connection was established using the SSH public and private key mechanism.

## 10. Conclusion

The experiment demonstrated the process of generating RSA key pairs and configuring passwordless SSH authentication between Linux systems. SSH key-based authentication provides a secure and convenient way to access remote systems without repeatedly entering account passwords. It is widely used in Linux system administration, server management, and automation.
