from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_file(file_path):
    with open(file_path, "rb") as f:
        data = f.read()

    encrypted = cipher.encrypt(data)
    with open(file_path, "wb") as f:
        f.write(encrypted)

    os.rename(file_path, file_path + ".locked")

if __name__ == "__main__":
    encrypt_file("test.txt")
