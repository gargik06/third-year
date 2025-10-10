import math

def encrypt_columnar(message, key):
    msg = message.replace(" ", "")
    col = len(key)
    row = math.ceil(len(msg)/col)
    pad = row * col - len(msg)
    msg += '_' * pad

    matrix = [list(msg[i:i+col]) for i in range(0, len(msg), col)]
    key_order = sorted([(k,i) for i,k in enumerate(key)])
    
    cipher = ""
    for k, col_idx in key_order:
        for r in range(row):
            cipher += matrix[r][col_idx]
    return cipher

msg = "network security"
key = "tycs"
print("Original:", msg)
print("Key:", key)
print("Encryption:", encrypt_columnar(msg, key))
