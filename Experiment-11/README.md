# Experiment 11: Capture and Analyze Encrypted VPN Traffic Using Wireshark

## 1. Aim

To capture and analyze encrypted VPN traffic using Wireshark and compare it with unencrypted network communication.

## 2. Introduction

A Virtual Private Network (VPN) provides secure communication by creating an encrypted tunnel between a user's device and a VPN server. It helps protect transmitted information from unauthorized monitoring.

Wireshark is a network packet analyzer used to capture and inspect network traffic. In this experiment, Wireshark was used to examine HTTP and HTTPS communication without a VPN and encrypted WireGuard traffic with a VPN.

## 3. Software Requirements

- Wireshark
- Proton VPN (Free Version)
- Windows Operating System
- Web Browser
- Command Prompt
- Active Internet Connection

## 4. Theory

**HTTP (Hypertext Transfer Protocol):** HTTP transmits information without application-layer encryption. Network packets may expose readable requests, headers, and transmitted content.

**HTTPS (Hypertext Transfer Protocol Secure):** HTTPS uses TLS encryption to protect communication between a client and a web server.

**VPN (Virtual Private Network):** A VPN establishes an encrypted tunnel to protect network traffic between the client and VPN server.

**WireGuard:** WireGuard is a modern VPN protocol that uses cryptographic techniques to provide secure and efficient network communication.

## 5. Experimental Procedure

### Part A: Capturing Network Traffic Without VPN

**Step 1: Start Wireshark**

1. Open Wireshark.
2. Select the active Wi-Fi network interface.
3. Start capturing network packets.

**Screenshot 1: Wireshark Start**

*Insert: `Wireshark-start.png`*

**Step 2: Generate HTTP Traffic**

1. Ensure Proton VPN is disconnected.
2. Open an HTTP website or generate an HTTP request using Command Prompt.

```cmd
curl.exe -v http://neverssl.com/
```

3. Apply the Wireshark display filter:

```text
http
```

4. Observe HTTP packets and inspect the request information.

**Screenshot 2: HTTP Website Without VPN**

*Insert: `http website without VPN.png`*

**Screenshot 3: Unencrypted HTTP Traffic Without VPN**

*Insert the screenshot showing HTTP packets and readable request information.*

**Step 3: Capture HTTPS Traffic**

1. Keep the VPN disconnected.
2. Open `https://example.com` in the browser.
3. Apply the display filter:

```text
tls
```

4. Observe the TLS packets and available handshake information.

**Screenshot 4: HTTPS Traffic Without VPN**

*Insert: `HTTPS Traffic Without VPN.png`*

### Part B: Capturing Encrypted Traffic With VPN

**Step 4: Connect Proton VPN**

1. Open Proton VPN.
2. Log in using the free account.
3. Click Quick Connect.
4. Wait until the VPN connection is established.
5. Verify the connected status.

**Screenshot 5: VPN Connected**

*Insert: `VPN Connected.png`*

**Step 5: Capture VPN Network Traffic**

1. Open Wireshark.
2. Select the physical Wi-Fi network interface.
3. Start a new packet capture.
4. Generate network traffic by accessing an HTTPS website.
5. Apply the following display filter:

```text
udp
```

6. Identify the WireGuard transport packets.

**Step 6: Analyze Encrypted WireGuard Packets**

1. Select a WireGuard Transport Data packet.
2. Expand the WireGuard Protocol section.
3. Observe the receiver identifier, counter, and encrypted packet field.
4. Examine the source IP, destination IP, and UDP ports.

**Screenshot 6: Encrypted VPN Traffic Analysis Using WireGuard**

*Insert: `Encrypted VPN Traffic Analysis Using WireGuard.png`*

## 6. Packet Analysis and Observations

The following details were observed in the captured WireGuard packet:

| Parameter | Observed Value |
|---|---|
| Packet Number | 57 |
| Source IP Address | 192.168.29.16 |
| Destination IP Address | 212.8.243.129 |
| Transport Protocol | UDP |
| VPN Protocol | WireGuard |
| Source Port | 58272 |
| Destination Port | 443 |
| Packet