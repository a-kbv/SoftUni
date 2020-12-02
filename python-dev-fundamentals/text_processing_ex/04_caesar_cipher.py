text = input()

result = ""

for char in range(len(text)):
    new_char = ord(text[char]) + 3
    result += chr(new_char)

print(result)