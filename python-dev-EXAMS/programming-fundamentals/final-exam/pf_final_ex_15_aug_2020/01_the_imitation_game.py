def move(message, n_letters):
    split_l = message[:n_letters]
    split_r = message[n_letters:]
    return split_r + split_l

def insert(message, index, value):
    split_l = message[:index]
    split_r = message[index:]
    return split_l + value + split_r

def changeall(message, substring, replacement):
    return message.replace(substring, replacement)


def enigma():
    message = input()

    data = input()
    while not data == "Decode":
        data = data.split('|')
        commad = data[0]

        if commad == "Move":
            n_letters = int(data[1])
            message = move(message, n_letters)

        elif commad == "Insert":
            index = int(data[1])
            value = data[2]
            message = insert(message, index, value)

        elif commad == "ChangeAll":
            substring = data[1]
            replacement = data[2]
            message = changeall(message, substring, replacement)

        data = input()
    return message

print(f"The decrypted message is: {enigma()}")