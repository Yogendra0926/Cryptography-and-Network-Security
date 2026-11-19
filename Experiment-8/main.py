
import hashlib
import os
from cryptography.fernet import Fernet
key=Fernet.generate_key()
cipher=Fernet(key)
message=input("Enter your message: ")
hash_value=hashlib.sha256(message.encode()).hexdigest()
print("Original Message:", message)
print("SHA-256 Hash:", hash_value)
encrypted=cipher.encrypt(message.encode())
print("Encrypted Message:", encrypted.decode())
decrypted=cipher.decrypt(encrypted).decode()
print("Decrypted Message:", decrypted)
new_hash=hashlib.sha256(decrypted.encode()).hexdigest()
if hash_value==new_hash:
    print("Hash Verified Successfully!")
else:
    print("Hash Verification Failed!")
