from cryptography.fernet import Fernet

key = Fernet.generate_key() # genererar nyckeln

with open("secret.key", "wb") as key_file:
    key_file.write(key) # sparar nyckeln som en fil