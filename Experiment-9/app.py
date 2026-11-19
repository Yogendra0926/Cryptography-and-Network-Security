
import hashlib
import os
password = input("Enter Password: ")
hash_without_salt = hashlib.sha256(
    password.encode()
).hexdigest()
salt = os.urandom(16)
hash_with_salt = hashlib.sha256(
    salt + password.encode()
).hexdigest()
print("\n--- Password Hashing Results ---")
print("Original Password:", password)
print("\nWithout Salt:")
print("Hash:", hash_without_salt)
print("\nWith Salt:")
print("Salt:", salt.hex())
print("Hash:", hash_with_salt)
verify_hash = hashlib.sha256(
    salt + password.encode()
).hexdigest()

print("\nPassword Verification:",
      verify_hash == hash_with_salt)
