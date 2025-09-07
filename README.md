# Encryption/Decryption Demo (AES + RSA)

This project demonstrates encrypting and decrypting a short message using **symmetric (AES)** and **asymmetric (RSA)** encryption.

## How It Works

1. **AES (Symmetric)**
   - A random 256-bit AES key and IV are generated.
   - The input message is encrypted with AES in CFB mode.
   - The ciphertext is decrypted back to the original message using the same key.

2. **RSA (Asymmetric)**
   - A 2048-bit RSA private/public key pair is generated.
   - The input message is encrypted with the public key using OAEP padding with SHA-256.
   - The ciphertext is decrypted back using the private key.

## Input/Output
- Input message: "Hello, symmetric & asymmetric world!"
- Outputs include:
  - AES key (hex), IV (hex), ciphertext (hex), and decrypted plaintext.
  - RSA public key components (n, e), ciphertext (hex snippet), and decrypted plaintext.

## Requirements
- Python 3.8+
- Install dependencies:
  ```bash
  pip install cryptography
  ```

## Run
```bash
python encrypt_demo.py
```

Both symmetric and asymmetric encryption/decryption will run, and results will be saved in `encryption_output.txt`.
