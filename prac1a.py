def ceaser_encrypt(text, n):
    ans = ""
    for ch in text:
        if ch.isupper():
            ans += chr((ord(ch)-65 + n) % 26 + 65)
        elif ch.islower():
            ans += chr((ord(ch)-97 + n) % 26 + 97)
        else:
            ans += ch
    return ans

def ceaser_decrypt(cipher, n):
    return ceaser_encrypt(text, -n)

if __name__ == "__main__":
    text = input("Enter the text to encrypt: ")
    n = int(input("Enter the shift value: "))
    encrypted = ceaser_encrypt(text, n)
    print("Encrypted text: ", encrypted)
    print("Decrypted text: ", ceaser_decrypt(encrypted, n))
