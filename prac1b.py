def ceaser_encrypt(text, key):
    ans = ""
    shift = ord(key.lower()) - 97

    for ch in text:
        if ch.isupper():
            ans += chr((ord(ch) + shift - 65) % 26 + 65)
        elif ch.islower():
            ans += chr((ord(ch) + shift - 97) % 26 + 97)
        else:
            ans += ch
    return ans

text = input("Enter text to encrypt: ")
key = input("Enter the key: ")

if not (key.isalpha() and len(key) == 1):
    print("Invalid key")
else:
    print("encrytped: ", ceaser_encrypt(text, key))
