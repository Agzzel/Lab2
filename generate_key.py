from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key() # genererar nyckeln
    with open("secret.key", "wb") as key_file:
        key_file.write(key) # sparar nyckeln som en fil