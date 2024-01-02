from cryptography.fernet import Fernet

# Function to generate a key and save it into a file
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Function to encrypt the password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password)
    return encrypted_password

# Generate and write a new key
write_key()

# Load the key
key = open("key.key", "rb").read()

# Encrypt the password
encrypted_password = encrypt_password(b"<mypass>", key)

print(encrypted_password)