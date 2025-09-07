# encrypt_demo.py
# Demonstrates symmetric (AES) and asymmetric (RSA) encryption/decryption

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

# -----------------------------
# 1. Symmetric Encryption (AES)
# -----------------------------

# Generate random 256-bit AES key and IV
aes_key = os.urandom(32)
iv = os.urandom(16)

message = b"Hello, symmetric & asymmetric world!"

# Encrypt
cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
encryptor = cipher.encryptor()
aes_ciphertext = encryptor.update(message) + encryptor.finalize()

# Decrypt
decryptor = cipher.decryptor()
aes_plaintext = decryptor.update(aes_ciphertext) + decryptor.finalize()

# -----------------------------
# 2. Asymmetric Encryption (RSA)
# -----------------------------

# Generate RSA private/public key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()

# Encrypt with public key
rsa_ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Decrypt with private key
rsa_plaintext = private_key.decrypt(
    rsa_ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# -----------------------------
# Show Results
# -----------------------------
print("=== Input Message ===")
print(message.decode())

print("\n=== SYMMETRIC (AES) ===")
print("AES Key (hex):", aes_key.hex())
print("IV (hex):", iv.hex())
print("Ciphertext (hex):", aes_ciphertext.hex())
print("Decrypted:", aes_plaintext.decode())

print("\n=== ASYMMETRIC (RSA) ===")
print("Public Key (n):", public_key.public_numbers().n)
print("Public Key (e):", public_key.public_numbers().e)
print("Ciphertext (hex, first 80 chars):", rsa_ciphertext.hex()[:80] + "...")
print("Decrypted:", rsa_plaintext.decode())
