import math

p, q = 3, 7
n, phi = p * q, (p - 1) * (q - 1)
print("n =", n)

e = next(i for i in range(2, phi) if math.gcd(i, phi) == 1)
print("e =", e)

k, d = 2, ((2 * phi) + 1) / e
print("d =", d)

print(f"public key: {e},{n}")
print(f"private key: {d},{n}")

msg = 11
print("original message:", msg)

c = math.fmod(pow(msg, e), n)
print("encrypted message:", c)

M = math.fmod(pow(c, d), n)
print("decrypted message:", M)
