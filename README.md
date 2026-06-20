# Visual Cryptography Engine (2,2 Scheme)

An implementation of Naor and Shamir's Visual Secret Sharing Scheme using Python. This project splits a binary secret image into two completely random shares. Individually, each share leaks 0% information and looks like static noise. The secret is only revealed when both digital layers are stacked together.

## ⚙️ Core Engineering Concepts
- **Matrix Expansion:** Expanding an $N \times M$ pixel matrix into a $2N \times 2M$ grid.
- **Perfect Secrecy:** Implementing random coin-toss probabilities to ensure mathematical un-linkability.
- **Bitwise Simulation:** Layering binary matrices using spatial pixel manipulation.

## 🚀 How to Run
1. Place a black and white image named `secret.png` in the root folder.
2. Run `python visual_crypto.py`.
3. Check `share1.png`, `share2.png`, and the revealed `reconstructed_secret.png`.
