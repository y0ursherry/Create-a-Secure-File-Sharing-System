import os
from cryptography.fernet import Fernet

# 1. Cryptographic Key & Mock Cloud Bucket Setup
ENCRYPTION_KEY = Fernet.generate_key()
cipher_suite = Fernet(ENCRYPTION_KEY)
MOCK_CLOUD_BUCKET = {}

def encrypt_and_upload(filename, file_content):
    """Encrypts file content locally and uploads it to mock cloud storage."""
    # End-to-End Encryption
    encrypted_data = cipher_suite.encrypt(file_content.encode('utf-8'))
    # Simulating upload to Cloud (AWS S3 / GCP Blob)
    MOCK_CLOUD_BUCKET[filename] = encrypted_data
    return True

def generate_signed_url(filename):
    """Generates a secure, time-limited simulated signed URL."""
    if filename in MOCK_CLOUD_BUCKET:
        secure_token = os.urandom(16).hex()
        signed_url = f"https://s3.internee.pk/secure-vault/{filename}?X-Amz-Expires=3600&token={secure_token}"
        return signed_url
    return None

def download_and_decrypt(filename):
    """Downloads encrypted content from cloud and decrypts it locally."""
    if filename in MOCK_CLOUD_BUCKET:
        encrypted_data = MOCK_CLOUD_BUCKET[filename]
        # Decrypting locally on client side
        decrypted_data = cipher_suite.decrypt(encrypted_data).decode('utf-8')
        return decrypted_data
    return None

def main():
    while True:
        print("\n--- SECURE FILE SHARING SYSTEM ---")
        print("1. Upload File (With End-to-End Encryption)")
        print("2. Generate Secure Signed URL for File")
        print("3. Download & Decrypt File")
        print("4. Exit")
        
        choice = input("Select an option (1-4): ").strip()
        
        if choice == '1':
            filename = input("Enter file name (e.g., report.txt): ").strip()
            content = input("Enter confidential content for the file: ")
            print(f"\n[Client] Encrypting '{filename}' locally...")
            if encrypt_and_upload(filename, content):
                print(f"[Cloud] Successfully uploaded encrypted '{filename}' to secure storage.")
                
        elif choice == '2':
            filename = input("Enter filename for Signed URL: ").strip()
            url = generate_signed_url(filename)
            if url:
                print(f"\nGenerated Secure Signed URL (Expires in 1 Hour):")
                print(f"{url}")
            else:
                print("\nError: File not found in secure storage.")
                
        elif choice == '3':
            filename = input("Enter filename to download: ").strip()
            print(f"\n[Cloud] Fetching encrypted blocks for '{filename}'...")
            decrypted_content = download_and_decrypt(filename)
            if decrypted_content:
                print("[Client] Decrypting payload using local cryptographic key...")
                print(f"Decrypted File Content: {decrypted_content}")
            else:
                print("\nError: Access Denied or File does not exist.")
                
        elif choice == '4':
            print("\nGoodbye!")
            break
        else:
            print("\nError: Invalid choice, please try again.")

if __name__ == "__main__":
    main()