---

## 🌐 Module 2: Network-Layer AES-GCM Socket Cipher

A secure client-server network architecture executing cryptographic payload transport over TCP sockets using **AES-GCM (Authenticated Encryption with Associated Data)**.

### 🧪 Technical Milestones Achieved
- **Authenticated Symmetric Ciphers:** Implemented a rigid 256-bit AES block structure ensuring data confidentiality and cryptanalysis resistance.
- **Tamper Detection & Integrity:** Leveraged GCM authenticated mode to detect network packet injections, mid-stream modifications, or replay attacks.
- **Dynamic Initialization Vectors:** Generated unique 12-byte cryptographically secure nonces (`os.urandom`) per session to eliminate replay vulnerabilities.

### 🚀 Execution Tracking
1. Initialize the background intercept port: `python 02-socket-packet-cipher/server.py`
2. Execute the transmission payload in a separate console: `python 02-socket-packet-cipher/client.py`
