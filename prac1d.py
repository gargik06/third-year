string = input("Enter a string: ")

def RailFence(text):
    result = ""
    for i in range(len(string)):
        if(i % 2 == 0):
            result += string[i]
    for i in range(len(string)):
        if(i % 2 != 0):
            result += string[i]
    return result

print(RailFence(string))
