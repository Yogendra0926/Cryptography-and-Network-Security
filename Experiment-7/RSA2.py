
prime1 = 61
prime2 = 53
modulus = prime1 * prime2
totient = (prime1 - 1) * (prime2 - 1)
public_exp = 1019
private_exp = pow(public_exp, -1, totient)
print("RSA Key Generation")
print("-------------------")
print("First prime number:", prime1)
print("Second prime number:", prime2)
print("Modulus (n):", modulus)
print("Euler Totient:", totient)
print("\nPublic Key:", (public_exp, modulus))
print("Private Key:", (private_exp, modulus))
plain_text = int(input(f"\nEnter plaintext (number less than {modulus}): "))
encrypted_text = pow(plain_text, public_exp, modulus)
recovered_text = pow(encrypted_text, private_exp, modulus)
print("\nRSA Encryption Result")
print("---------------------")
print("Input Message:", plain_text)
print("Encrypted Message:", encrypted_text)
print("Decrypted Message:", recovered_text)
