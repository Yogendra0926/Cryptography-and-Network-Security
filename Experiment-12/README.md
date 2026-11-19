# Experiment: Analysis of Secure and Insecure Network Protocols Using Wireshark

## 1. Aim

To capture and analyze network packets using Wireshark to identify secure and insecure communication protocols and evaluate their security implications.

## 2. Introduction

Wireshark is an open-source network protocol analyzer used to capture and inspect network traffic in real time.

Network communication uses different protocols to transfer data between devices. Some protocols, such as HTTP, transmit data without encryption, while others, such as HTTPS, use encryption to protect transmitted information.

In this experiment, HTTP and HTTPS network traffic are captured and analyzed using Wireshark to understand the differences between secure and insecure communication.

## 3. Software Requirements

- Wireshark
- Windows or Linux operating system
- Internet connection
- Web browser
- Command Prompt (CMD)

## 4. Theory

### HTTP (Hypertext Transfer Protocol)

HTTP is an application-layer protocol used for communication between web browsers and servers.

- Default Port: 80
- Data Transmission: Unencrypted
- Security: Insecure
- Vulnerability: Data interception and modification

### HTTPS (Hypertext Transfer Protocol Secure)

HTTPS is the secure version of HTTP that uses TLS encryption to protect data during transmission.

- Default Port: 443
- Data Transmission: Encrypted
- Security: Secure when properly configured
- Protection: Confidentiality, integrity, and server authentication

### TLS (Transport Layer Security)

TLS is a cryptographic protocol that provides secure communication over a network.

The TLS handshake establishes the security parameters required for encrypted communication.

Important TLS handshake messages include:

1. **Client Hello:** The client initiates the TLS handshake and provides supported TLS versions and cipher suites.
2. **Server Hello:** The server selects the TLS parameters for the connection.
3. **Application Data:** Encrypted application data is transmitted after the handshake establishes the required keys.

## 5. Procedure

### Step 1: Open Wireshark

1. Launch Wireshark.
2. Select the active Wi-Fi or Ethernet interface.
3. Click Start Capture to begin capturing network packets.

### Step 2: Capture HTTP Traffic

Open Command Prompt and execute:

```cmd
curl.exe -v http://neverssl.com/
```

Return to Wireshark and apply the display filter:

```text
http
```

Observe the HTTP request and response packets.

### Step 3: Analyze HTTP Packets

1. Select an HTTP GET request packet.
2. Expand the Hypertext Transfer Protocol section.
3. Observe the request method, host, and request URI.
4. Right-click the packet and select **Follow → HTTP Stream**.
5. Examine the readable HTTP request and response data.

**Observation:** HTTP communication transmits application data without encryption, allowing readable content to be observed in captured packets.

### Step 4: Capture HTTPS Traffic

Stop the current capture and start a new capture on the active network interface.

Open Command Prompt and execute:

```cmd
curl.exe -v --http1.1 https://example.com/
```

Apply the following Wireshark display filter:

```text
tls
```

Observe the TLS packets associated with HTTPS communication.

### Step 5: Analyze TLS Client Hello

Apply the display filter:

```text
tls.handshake.type == 1
```

Select a Client Hello packet and expand:

- Transport Layer Security
- TLS Record Layer
- Handshake Protocol: Client Hello

Observe the supported TLS versions and cipher suites.

Examples of modern cipher suites include:

```text
TLS_AES_128_GCM_SHA256
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
```

### Step 6: Analyze TLS Server Hello

Apply the display filter:

```text
tls.handshake.type == 2
```

Select a Server Hello packet and observe:

- Selected cipher suite
- Negotiated TLS version
- Server handshake parameters

These details help determine which cryptographic settings were negotiated for the connection.

### Step 7: Analyze Encrypted Application Data

Apply the display filter:

```text
tls.record.content_type == 23
```

Observe the TLS Application Data records.

Unlike HTTP, encrypted HTTPS application content cannot normally be read directly from the packet capture without the appropriate decryption keys.

### Step 8: Save the Captured Packets

Stop packet capture and save the results using:

**File → Save As**

Save the captures as:

```text
HTTP_Capture.pcapng
HTTPS_Capture.pcapng
```

## 6. Comparison of Secure and Insecure Protocols

| Feature | HTTP | HTTPS |
|---|---|---|
| Full Form | Hypertext Transfer Protocol | Hypertext Transfer Protocol Secure |
| Default Port | 80 | 443 |
| Encryption | No | Yes, using TLS |
| Data Visibility | Readable plaintext | Encrypted application content |
| Data Confidentiality | Not provided | Provided |
| Data Integrity | Not cryptographically protected | Protected by TLS |
| Authentication | No built-in server authentication | TLS certificate-based server authentication |
| Security | Insecure | Secure when properly configured |

## 7. Wireshark Display Filters

| Filter | Purpose |
|---|---|
| `http` | Display HTTP packets |
| `tls` | Display TLS packets |
| `tcp.port == 80` | Display TCP port 80 traffic |
| `tcp.port == 443` | Display TCP port 443 traffic |
| `tls.handshake.type == 1` | Display TLS Client Hello |
| `tls.handshake.type == 2` | Display TLS Server Hello |
| `tls.record.content_type == 23` | Display TLS Application Data |
| `dns` | Display DNS packets |

## 8. Security Implications

### Insecure Communication

- HTTP transmits application data without encryption.
- Attackers with access to network traffic may intercept readable information.
- Unencrypted communication can expose sensitive information.
- HTTP traffic is vulnerable to interception and modification.

### Secure Communication

- HTTPS uses TLS encryption to protect transmitted application data.
- TLS provides confidentiality and integrity.
- Digital certificates help authenticate servers.
- Secure cipher suites protect communication against passive eavesdropping.
- Proper TLS configuration reduces the risk of man-in-the-middle attacks.

## 9. Observation

During the experiment, HTTP packets were captured using Wireshark.

The captured traffic included:

```text
GET / HTTP/1.1
HTTP/1.1 200 OK
```

The HTTP request was transmitted using TCP destination port 80, and the request information was readable in the packet details.

HTTPS/TLS analysis involves examining Client Hello, Server Hello, and encrypted Application Data packets to understand how secure communication is established.

## 10. Result

HTTP traffic was successfully captured and analyzed using Wireshark. The captured packets demonstrated that HTTP transmits readable application data without encryption.

The TLS analysis procedure was used to examine how HTTPS negotiates encryption parameters and protects application data during transmission.

The comparison demonstrates the security advantages of HTTPS over HTTP.

## 11. Conclusion

The experiment demonstrated how Wireshark can be used to capture and analyze network packets to identify secure and insecure communication protocols.

HTTP communication was found to transmit readable data without encryption, making it vulnerable to interception and modification.

HTTPS uses TLS to establish encrypted communication through a handshake process involving Client Hello, Server Hello, and cryptographic parameter negotiation.

The experiment highlights the importance of using secure communication protocols to protect data confidentiality, integrity, and authentication during network transmission.
