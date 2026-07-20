# Task 4: Secure File Sharing System

This project is a Secure File Sharing System built in Python. It ensures safe file exchanges using End-to-End Encryption (E2EE) and simulated Cloud Storage Pre-Signed URLs. Developed during my Cybersecurity Internship at Internee.pk.

## Features
* **End-to-End Encryption:** Files are encrypted locally before being uploaded.
* **Simulated Cloud Storage:** Emulates cloud bucket storage for uploading and downloading files.
* **Pre-Signed URLs:** Generates secure, time-limited token links for safe sharing.
* **Secure Decryption:** Encrypted files are downloaded and decrypted safely on the client side.

## How to Run
1. Install dependency:
   ```bash
   pip install cryptography
2. Run the Application:
   ```bash
   python secure_share.py
   
