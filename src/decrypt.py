import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

# Load environment variables from .env file only once
load_dotenv()

def decrypt_credentials():
    """Decrypts and returns the stored username, password, and URL from .env."""
    
    # Retrieve encryption key from .env
    key = os.getenv("ENCRYPTION_KEY")
    if not key:
        raise ValueError("ENCRYPTION_KEY is missing from .env file.")

    try:
        cipher_suite = Fernet(key.encode())
    except Exception as e:
        raise ValueError("Invalid encryption key: Ensure it's correctly stored.") from e

    # Retrieve encrypted credentials from .env
    encrypted_username = os.getenv("ENCRYPTED_USERNAME")
    encrypted_password = os.getenv("ENCRYPTED_PASSWORD")
    URL = os.getenv("URL")

    if not encrypted_username or not encrypted_password:
        raise ValueError("Encrypted credentials are missing from .env file.")
    if not URL:
        raise ValueError("URL is missing from .env file.")

    try:
        username = cipher_suite.decrypt(encrypted_username.encode()).decode()
        password = cipher_suite.decrypt(encrypted_password.encode()).decode()
    except Exception as e:
        raise ValueError("Decryption failed: Ensure the correct encryption key is used.") from e

    return username, password, URL

if __name__ == "__main__":
    try:
        user, pwd, url = decrypt_credentials()
        print(f"Decrypted Username: {user}")
        print(f"Decrypted Password: {pwd}")
        print(f"URL: {url}")
    except Exception as e:
        print(f"Error: {e}")
