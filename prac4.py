from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto import Random

key = RSA.generate(2048, Random.new().read)
private_key = key.export_key()
public_key = key.publickey().export_key()

message = "Hello World"

hashed = SHA256.new(message.encode())

signer = PKCS1_v1_5.new(RSA.import_key(private_key))
signature = signer.sign(hashed)

verifier = PKCS1_v1_5.new(RSA.import_key(public_key))
is_valid = verifier.verify(hashed, signature)

print("Digital Signature:", signature)
print("Is the signature valid?", is_valid)
