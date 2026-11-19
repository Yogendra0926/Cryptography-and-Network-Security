print("==== Diffie-Hellman Key Exchange ====")
p = 23
g = 5
print("Public Prime (p):", p)
print("Public Generator (g):", g)
# Private keys
a = int(input("\nEnter Alice's private key: "))
b = int(input("Enter Bob's private key: "))
# Alice calculates public key
A = pow(g, a, p)
# Bob calculates public key
B = pow(g, b, p)
print("Alice's public key:", A)
print("Bob's public key:", B)
# Shared secret calculated by Alice
secretAlice = pow(B, a, p)
# Shared secret calculated by Bob
secretBob = pow(A, b, p)
print("==== Shared Secret ====")
print("Alice's shared secret:", secretAlice)
print("Bob's shared secret:", secretBob)
if secretAlice == secretBob:
    print("\nKey Exchange Successful!")
    print("Both Alice and Bob have the same secret key.")
else:
    print("\nKey Exchange Failed!")