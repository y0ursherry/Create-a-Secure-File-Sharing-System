# Create-a-Secure-File-Sharing-System
# Task 4: Secure File Sharing System with End-to-End Encryption

This project is a Python-based implementation of a secure file-sharing application designed to protect sensitive data during transit and storage. Developed as part of my Cybersecurity Internship at Internee.pk, the system simulates cloud storage workflows (such as AWS S3 or GCP Storage) while maintaining strict cryptographic boundaries.

## Key Features

* **End-to-End Encryption (E2EE):** Encrypts files locally on the client machine before any data is sent to the storage layer, ensuring zero-knowledge privacy.
* **Simulated Cloud Storage Vault:** Emulates cloud bucket structures to programmatically handle data storage and object retrieval.
* **Pre-Signed URLs:** Generates dynamic, time-limited, and tokenized access links to safely share assets with external parties without exposing the storage backbone.
* **Local Client Decryption:** Fetches encrypted blocks from the vault and applies cryptographic keys strictly on the client side to recover the original content.

## Architecture & Cryptography

The system utilizes symmetric cryptography provided by the `cryptography` library. 

1. **Fernet (AES-128 in CBC mode):** Used for encrypting and decrypting file data with a secure, 128-bit key.
2. **Secure Tokenization:** Utilizes cryptographically secure random bytes to append unique authorization tokens to simulated S3 endpoints.

## Project Structure

* `secure_share.py` - Core source code containing the encryption modules, cloud simulation, and terminal user interface.
* `README.md` - Technical documentation for the repository.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Secure-File-Sharing-System.git](https://github.com/YOUR_USERNAME/Secure-File-Sharing-System.git)
   cd Secure-File-Sharing-System
