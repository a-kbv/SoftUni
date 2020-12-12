
def phone_book():
    phone_dict = {}
    data = input()

    while not data[0].isdigit():
        data = data.split('-')
        phone_dict[data[0]] = data[1]
        data = input()

    n = int(data)
    for _ in range(n):
        name = input()
        if name in phone_dict:
            print(f"{name} -> {phone_dict[name]}")
        else:
            print(f"Contact {name} does not exist.")

phone_book()