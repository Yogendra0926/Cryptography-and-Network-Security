p=61
q=53
n=p*q
phi=(p-1)*(q-1)
e=1019
d=pow(e,-1,phi)
print(f"p={p}")
print(f"q={q}")
print(f"n={n}")
print(f"phi(n)={phi}")
print(f"public key ={e},{n}")
print(f"private key ={d},{n}")
message=int(input(f"enter your numerical plaintext less than {n}"))
ciphertext = pow(message, e, n)
decrypted_message = pow(ciphertext, d, n)
print(f"original message is {message}")
print(f"ciphertext message is {ciphertext}")
print(f"decrypted message is {decrypted_message}")