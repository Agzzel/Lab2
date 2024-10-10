from cryptography.fernet import Fernet

with open("secret.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key) # instansierar Fernet med key som argument

message = "Hemligt meddelande".encode() # kodar meddelandet till binär form
cipher_text = cipher.encrypt(message)
print(f"Krypterad text:{cipher_text}")

with open("encoded_msg.enc", "wb") as encoded_file:
    encoded_file.write(cipher_text) # sparar det krypterade meddelandet som en fil

# dekryptering

with open("encoded_msg.enc", "rb") as encrypted_file:
    message = encrypted_file.read() # spara det krypterade meddelandet i message

decrypted_text = cipher.decrypt(message)
print(f"Dekrypterad text:{decrypted_text.decode()}")