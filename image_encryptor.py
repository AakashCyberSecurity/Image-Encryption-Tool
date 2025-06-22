from cryptography.fernet import Fernet
from PIL import Image
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved as 'secret.key'")

def load_key():
    return open("secret.key", "rb").read()

def encrypt_image(file_path):
    if not os.path.isfile(file_path):
        print("❌ Invalid file path. Please provide a valid image file.")
        return

    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open("encrypted_image.enc", "wb") as enc_file:
        enc_file.write(encrypted)

    print("[+] Image encrypted and saved as 'encrypted_image.enc'")

def decrypt_image(enc_path, output_name="decrypted_image.jpg"):
    key = load_key()
    fernet = Fernet(key)

    with open(enc_path, "rb") as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(output_name, "wb") as dec_file:
        dec_file.write(decrypted)

    print(f"[+] Image decrypted and saved as '{output_name}'")

if __name__ == "__main__":
    while True:
        print("\n🔐 Image Encryption Tool")
        print("1. Generate Key")
        print("2. Encrypt Image")
        print("3. Decrypt Image")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            generate_key()
        elif choice == "2":
            path = input("Enter image file path: ")
            encrypt_image(path)
        elif choice == "3":
            path = input("Enter encrypted file path: ")
            name = input("Enter output image name (e.g., output.jpg): ")
            decrypt_image(path, name)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Try again.")
