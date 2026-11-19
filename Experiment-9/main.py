
import hashlib
import secrets
import hmac
def hash_without_salt(password):
    return hashlib.sha256(password.encode()).hexdigest()
def hash_with_salt(password):
    salt = secrets.token_bytes(16)
    hashed = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000
    )
    return salt, hashed
def verify_password(password, salt, stored_hash):
    new_hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        100000
    )
    return hmac.compare_digest(new_hash, stored_hash)
password = input("Enter your password: ")
hash1 = hash_without_salt(password)
hash2 = hash_without_salt(password)
print("--- WITHOUT SALT ---")
print("Hash 1:", hash1)
print("Hash 2:", hash2)
print("Same Hash:", hash1 == hash2)
salt1, salted_hash1 = hash_with_salt(password)
salt2, salted_hash2 = hash_with_salt(password)
print("--- WITH SALT ---")
print("Salt 1:", salt1.hex())
print("Hash 1:", salted_hash1.hex())
print("Salt 2:", salt2.hex())
print("Hash 2:", salted_hash2.hex())
print("Same Hash:", salted_hash1 == salted_hash2)
print("--- PASSWORD VERIFICATION ---")
check = input("Re-enter your password: ")
if verify_password(check, salt1, salted_hash1):
    print("Password Verified Successfully!")
else:
    print("Incorrect Password!")
print("--- DICTIONARY ATTACK DEMO ---")
common_passwords = [
    "123456",
    "password",
    "admin123",
    "hello123",
    "qwerty"
]
target_hash=hash_without_salt("password")
for word in common_passwords:
    if hash_without_salt(word)==target_hash:
        print("Password found:",word)
        break
