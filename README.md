# 🔐 Image Encryption Tool

A Python-based utility to encrypt and decrypt image files using AES encryption with Fernet.

## 🛡️ Features
- Encrypts image files securely
- Decrypts encrypted images with the correct key
- Prevents unauthorized access and tampering
- CLI-based tool with easy-to-follow prompts

## 📦 Requirements
- Python 3.x
- cryptography
- Pillow

Install dependencies:
```bash
pip install cryptography pillow
```

## 🚀 How to Use

1. Run the script:
```bash
python image_encryptor.py
```

2. Options:
- `1`: Generate a new encryption key
- `2`: Encrypt an image file (`.jpg`, `.png`, etc.)
- `3`: Decrypt an encrypted image file
- `4`: Exit

## 📂 Output Files
- `secret.key`: Encryption key (keep it safe!)
- `encrypted_image.enc`: Encrypted file
- `decrypted_image.jpg`: Decrypted image

## 📄 License
MIT License
