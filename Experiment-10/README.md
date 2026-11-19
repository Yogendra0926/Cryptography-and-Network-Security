# Experiment: Capturing HTTPS Network Traffic and Analyzing TLS Handshake Using Wireshark
## 1. Aim
To capture HTTPS network traffic using Wireshark and analyze the TLS handshake, digital certificates, cipher suites, and encrypted application data.

## 2. Software Required
- Wireshark
- Google Chrome / Microsoft Edge
- Windows Operating System
- Internet Connection

## 3. Introduction
HTTPS (HyperText Transfer Protocol Secure) is used to secure communication between a web browser and a web server. It uses TLS (Transport Layer Security) to provide confidentiality, integrity, and authentication.

Wireshark is a network protocol analyzer used to capture and inspect network packets. It helps analyze the TLS handshake process, identify negotiated cipher suites, inspect certificates, and observe encrypted communication.

## 4. Procedure
1. Open Wireshark and select the active Wi-Fi or Ethernet network interface.
2. Start capturing network traffic.
3. Open a web browser and visit `https://www.google.com`.
4. Refresh the webpage and wait for a few seconds.
5. Stop the packet capture in Wireshark.
6. Apply the display filter `tls` or `tcp.port == 443`.
7. Find and analyze the **Client Hello** packet using the filter:
   `tls.handshake.type == 1`
8. Find and analyze the **Server Hello** packet using the filter:
   `tls.handshake.type == 2`
9. Observe the TLS version, supported and negotiated cipher suites, and handshake details.
10. View the website's digital certificate through the browser's security information.
11. Observe encrypted application data using the filter `tls.app_data`.

## 5. Observation
During the capture, the following details were observed:

- HTTPS communication was established over port 443.
- Client Hello was sent by the browser.
- Server Hello was received from the server.
- TLS protocol version and cipher suite were negotiated.
- The website's digital certificate was found to be valid.
- Application data was transmitted in encrypted form.

## 6. Result
HTTPS traffic was successfully captured and analyzed using Wireshark. The TLS handshake, Client Hello, Server Hello, cipher suite negotiation, digital certificate, and encrypted application data were examined.

## 7. Conclusion
This experiment demonstrated how Wireshark can be used to analyze secure HTTPS communication. It helped understand the TLS handshake process, certificate-based authentication, cipher suite negotiation, and how TLS protects application data from being read in plain text during network transmission.

