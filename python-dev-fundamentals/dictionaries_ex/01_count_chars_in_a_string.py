text = input()
dict = {}

for char in text:
    if char not in dict and not char == " ":
        dict[char] = 1
    elif char in dict and not char == " ":
        dict[char] += 1

for key,value in dict.items():
    print(f"{key} -> {value}")
