def take_odd_pw(password):
    password = ''.join([password[index] for index in range(len(password)) if not index % 2 == 0])
    print(password)
    return password

def cut_pw(password, index, lenght):
    left_side = password[:index]
    right_side = password[index+lenght:]
    password = left_side + right_side
    print(password)
    return password

def substitute_pw(password, substring, substitute):
    if substring in password:
        password = password.split(f'{substring}')
        password = f'{substitute}'.join(password)
        print(password)
        return password
    else:
        print("Nothing to replace!")
        return password

def password_reset():
    password = input()

    data = input()
    while not data == "Done":
        data = data.split(' ')
        command = data[0]

        if command == "TakeOdd":
            password = take_odd_pw(password)

        elif command == "Cut":
            index = int(data[1])
            lenght = int(data[2])
            password = cut_pw(password, index, lenght)

        elif command == 'Substitute':
            substring = data[1]
            substitute = data[2]
            password = substitute_pw(password, substring, substitute)

        data = input()
    return f'Your password is: {password}'

print(password_reset())