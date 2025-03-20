from cryptography.fernet import Fernet
import os
import sys

def encrypt_credentials(username, password):
    """Encrypts and stores the credentials in a .env file."""
    # Generate a new encryption key
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)

    # Encrypt credentials
    encrypted_username = cipher_suite.encrypt(username.encode()).decode()
    encrypted_password = cipher_suite.encrypt(password.encode()).decode()

    # Store credentials securely in a .env file
    with open(".env", "w") as env_file:
        env_file.write(f"ENCRYPTION_KEY={key.decode()}\n")
        env_file.write(f"ENCRYPTED_USERNAME={encrypted_username}\n")
        env_file.write(f"ENCRYPTED_PASSWORD={encrypted_password}\n")

    print("Encryption key and encrypted credentials saved to .env.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python encrypt.py <username> <password>")
        sys.exit(1)

    user, pwd = sys.argv[1], sys.argv[2]
    encrypt_credentials(user, pwd)
