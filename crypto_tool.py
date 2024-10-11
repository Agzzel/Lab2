from generate_key import create_key
from cryptography.fernet import Fernet

create_key()
with open("secret.key", "rb") as key_file:
    key = key_file.read()

def encrypt():
        cipher = Fernet(key) # instansierar Fernet med key som argument
        message = input("Ange meddelande: ").encode()
        cipher_text = cipher.encrypt(message)
        with open("encoded_msg.enc", "wb") as encoded_file:
            encoded_file.write(cipher_text) # sparar det krypterade meddelandet som en fil


def decrypt():
    with open("encoded_msg.enc", "rb") as encrypted_file:
        message = encrypted_file.read() # spara det krypterade meddelandet i message
        cipher = Fernet(key)
        cipher_text = cipher.decrypt(message)
        print(cipher_text)


