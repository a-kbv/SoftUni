def contains(data, activation_key):
    substring = data[1]
    if substring in activation_key:
        return f"{activation_key} contains {substring}"
    return "Substring not found!"

def flip(data, activation_key):
    u_l = data[1]
    start = int(data[2])
    end = int(data[3])

    if u_l == "Upper":
        activation_key = activation_key[:start] + activation_key[start:end].upper() + activation_key[end:]
    else:
        activation_key = activation_key[:start] + activation_key[start:end].lower() + activation_key[end:]
    return activation_key


def slice(data, activation_key):
    start = int(data[1])
    end = int(data[2])
    activation_key = activation_key[:start] + activation_key[end:]
    return activation_key


activation_key = input()

data = input()

while not data == "Generate":

    data = data.split(">>>")

    if data[0] == "Slice":
        activation_key = slice(data, activation_key)
        print(activation_key)

    if data[0] == "Flip":
        activation_key = flip(data, activation_key)
        print(activation_key)

    if data[0] == "Contains":
        result = contains(data, activation_key)
        print(result)

    data = input()

print(f"Your activation key is: {activation_key}")