
def insert_space(message, index):
    left_part = message[:index]
    right_part = message[index:]
    message = left_part + " " + right_part
    print(message)
    return message

def reverse(message, substring):
    if substring in message:
        index = message.index(substring)
        left_part = message[:index]
        right_part = message[index + len(substring):]
        message = left_part + right_part + substring[::-1]
        print(message)
        return message
    else:
        print("error")
        return message

def change_all(message, substring, replacement):
    message = message.replace(substring, replacement)
    print(message)
    return message

def process_command(message, line):
    command = line.split(":|:")

    if command[0] == "ChangeAll":
        substing = command[1]
        replacement = command[2]
        return change_all(message, substing, replacement)

    elif command[0] == "Reverse":
        substring = command[1]
        return reverse(message, substring)

    elif command[0] == "InsertSpace":
        index = int(command[1])
        return insert_space(message, index)

if __name__ == "__main__":
    message = input()
    line = input()
    while not line == "Reveal":
        message = process_command(message, line)

        line = input()
    print(f"You have a new text message: {message}")