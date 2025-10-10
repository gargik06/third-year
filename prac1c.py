def StringEncryption(text, key):
    cipherText = ""
    cipher = []
    for i in range(len(key)):
        shift = (ord(text[i]) - ord('A') + ord(key[i]) - ord('A'))
        cipher.append(shift)
    for val in cipher:
        cipherText += chr(val + ord('A'))
    return cipherText
plainText = "HelloTYCS"
key = "MONEYBANK"
encryptedText = StringEncryption(plainText.upper(), key.upper())
print("cipherText: ", encryptedText)
