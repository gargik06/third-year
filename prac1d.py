text = input("Enter a Text: ")

def RailFence(text):
    result = ""
    for i in range(len(text)):
        if(i % 2 == 0):
            result += text[i]
    for i in range(len(text)):
        if(i % 2 != 0):
            result += text[i]
    return result

print(RailFence(text))

